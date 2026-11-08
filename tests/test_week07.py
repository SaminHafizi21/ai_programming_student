"""
Week 07 Autograder: TicTacToe met Minimax & Alpha-Beta.

Test de publieke interface van de oplossing van de student:
- TicTacToe: __init__, is_valid_move, make_move, undo_move,
  possible_moves, check_winner, is_draw, minimax, find_best_move

De tests controleren enkel gedrag, niet hoe het geïmplementeerd is.
Studentencode die crasht of infinite loopt wordt netjes afgehandeld.
"""

import contextlib
import importlib
import threading

import pytest

MODULE_PATH = "exercises.week07.solution"

try:
    _mod = importlib.import_module(MODULE_PATH)
    TicTacToe = _mod.TicTacToe
except Exception as import_error:
    pytest.skip(
        f"solution.py kon niet geïmporteerd worden: {import_error}",
        allow_module_level=True,
    )

WEIGHTS = {
    "test_bord_init": 1,
    "test_is_valid_move": 1,
    "test_make_move": 1,
    "test_check_winner_rijen": 1,
    "test_check_winner_kolommen": 1,
    "test_check_winner_diagonalen": 1,
    "test_check_winner_geen_winnaar": 1,
    "test_is_draw": 1,
    "test_possible_moves": 1,
    "test_undo_move": 1,
    "test_minimax_basis_scores": 1,
    "test_minimax_forceert_win": 2,
    "test_minimax_alpha_beta_gelijk": 2,
    "test_minimax_depthlimit": 2,
    "test_find_best_move_wint": 2,
    "test_find_best_move_blokkeert": 2,
}


@contextlib.contextmanager
def time_limit(seconds: int = 5):
    """Beperk de duur van een blok code (tegen infinite loops).

    Gebruikt threading.Timer omdat SIGALRM niet werkt op Windows.
    """
    timeout_triggered = False

    def _raise():
        nonlocal timeout_triggered
        timeout_triggered = True

    timer = threading.Timer(seconds, _raise)
    timer.start()
    try:
        yield
        if timeout_triggered:
            raise TimeoutError(f"code duurde te lang (>{seconds}s)")
    finally:
        timer.cancel()


def _maak_bord(bezetting):
    """Hulpfunctie: maak een TicTacToe-bord met gegeven bezetting.

    `bezetting` is een dict {(r, c): 'X'|'O'} met de stenen die al staan.
    """
    spel = TicTacToe()
    for (r, c), speler in bezetting.items():
        spel.board[r][c] = speler
    return spel


# =============== Bord-initialisatie ===============


def test_bord_init():
    """Het bord is 3x3 met alle velden leeg."""
    spel = TicTacToe()
    with time_limit():
        assert len(spel.board) == 3
        for rij in spel.board:
            assert len(rij) == 3
            for veld in rij:
                assert veld == " ", f"veld moet leeg zijn, kreeg '{veld}'"


# =============== is_valid_move ===============


def test_is_valid_move():
    """is_valid_move geeft True voor leeg veld en False voor bezet veld."""
    spel = TicTacToe()
    with time_limit():
        assert spel.is_valid_move(0, 0) is True
        spel.board[0][0] = "X"
        assert spel.is_valid_move(0, 0) is False
        assert spel.is_valid_move(2, 2) is True
        assert spel.is_valid_move(-1, 0) is False
        assert spel.is_valid_move(3, 0) is False


# =============== make_move ===============


def test_make_move():
    """make_move plaatst de speler op de juiste positie."""
    spel = TicTacToe()
    with time_limit():
        spel.make_move(0, 0, "X")
        assert spel.board[0][0] == "X"
        spel.make_move(1, 1, "O")
        assert spel.board[1][1] == "O"
        spel.make_move(2, 2, "X")
        assert spel.board[2][2] == "X"


# =============== check_winner ===============


def test_check_winner_rijen():
    """Een rij van X of O wordt als winnaar herkend."""
    with time_limit():
        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (0, 2): "X"})
        assert spel.check_winner() == "X"

        spel = _maak_bord({(1, 0): "O", (1, 1): "O", (1, 2): "O"})
        assert spel.check_winner() == "O"


def test_check_winner_kolommen():
    """Een kolom van X of O wordt als winnaar herkend."""
    with time_limit():
        spel = _maak_bord({(0, 1): "X", (1, 1): "X", (2, 1): "X"})
        assert spel.check_winner() == "X"

        spel = _maak_bord({(0, 2): "O", (1, 2): "O", (2, 2): "O"})
        assert spel.check_winner() == "O"


def test_check_winner_diagonalen():
    """Diagonalen van X of O worden als winnaar herkend."""
    with time_limit():
        spel = _maak_bord({(0, 0): "X", (1, 1): "X", (2, 2): "X"})
        assert spel.check_winner() == "X"

        spel = _maak_bord({(0, 2): "O", (1, 1): "O", (2, 0): "O"})
        assert spel.check_winner() == "O"


def test_check_winner_geen_winnaar():
    """Zonder drie op een rij geeft check_winner None."""
    with time_limit():
        spel = TicTacToe()
        assert spel.check_winner() is None

        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (1, 1): "O"})
        assert spel.check_winner() is None


# =============== is_draw ===============


def test_is_draw():
    """is_draw geeft True als het bord vol is zonder winnaar."""
    with time_limit():
        bezet = {
            (0, 0): "X", (0, 1): "O", (0, 2): "X",
            (1, 0): "O", (1, 1): "X", (1, 2): "O",
            (2, 0): "O", (2, 1): "X", (2, 2): "O",
        }
        spel = _maak_bord(bezet)
        assert spel.is_draw() is True, "vol bord zonder winnaar is gelijkspel"

        spel2 = TicTacToe()
        assert spel2.is_draw() is False


# =============== possible_moves ===============


def test_possible_moves():
    """possible_moves geeft de juiste lijst van lege velden."""
    with time_limit():
        spel = TicTacToe()
        zetten = spel.possible_moves()
        assert len(zetten) == 9

        spel.board[0][0] = "X"
        zetten = spel.possible_moves()
        assert len(zetten) == 8
        assert (0, 0) not in zetten
        assert (0, 1) in zetten


# =============== undo_move ===============


def test_undo_move():
    """undo_move herstelt een leeg veld op de gegeven positie."""
    spel = TicTacToe()
    spel.board[0][0] = "X"
    with time_limit():
        spel.undo_move(0, 0)
    assert spel.board[0][0] == " ", "undo_move moet het veld leeg maken"


# =============== minimax ===============


def test_minimax_basis_scores():
    """minimax geeft correcte scores: 1 voor X-winst, -1 voor O-winst, 0."""
    with time_limit():
        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (0, 2): "X"})
        score = spel.minimax(0, True)
        assert score == 1

        spel = _maak_bord({(1, 0): "O", (1, 1): "O", (1, 2): "O"})
        score = spel.minimax(0, True)
        assert score == -1

        bezet = {
            (0, 0): "X", (0, 1): "O", (0, 2): "X",
            (1, 0): "O", (1, 1): "X", (1, 2): "O",
            (2, 0): "O", (2, 1): "X", (2, 2): "O",
        }
        spel = _maak_bord(bezet)
        score = spel.minimax(0, True)
        assert score == 0


def test_minimax_forceert_win():
    """minimax ziet dat X in één zet kan winnen (forceren)."""
    with time_limit():
        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (1, 0): "O"})
        score = spel.minimax(0, True)
    assert score == 1, "X moet kunnen winnen, minimax-score = 1"


def test_minimax_alpha_beta_gelijk():
    """minimax met alpha-beta geeft dezelfde score als minimax zonder."""
    scenario_borden = [
        {(0, 0): "X", (0, 1): "X", (1, 0): "O"},
        {(0, 0): "O", (0, 1): "O", (1, 0): "X"},
        {(1, 1): "X", (0, 0): "O"},
        {(0, 0): "X", (1, 1): "O", (2, 2): "X"},
    ]
    for bezetting in scenario_borden:
        with time_limit():
            spel = _maak_bord(bezetting)
            score_plain = spel.minimax(0, True)
            spel2 = _maak_bord(bezetting)
            score_alphabeta = spel2.minimax(0, True,
                                            alpha=float("-inf"),
                                            beta=float("inf"))
        assert score_alphabeta == score_plain, (
            f"alpha-beta ({score_alphabeta}) verschilt van gewone minimax "
            f"({score_plain}) voor bord {bezetting}"
        )


def test_minimax_depthlimit():
    """Bij de maximale diepte wordt 0 gegeven; terminale staten winnen."""
    with time_limit():
        # Leeg bord met max_depth=2: alle bladeren zijn 0
        spel = TicTacToe()
        assert spel.minimax(0, True, max_depth=2) == 0

        # Terminale staten worden nog steeds herkend ondanks de dieptegrens
        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (0, 2): "X"})
        assert spel.minimax(0, True, max_depth=2) == 1

        spel = _maak_bord({(1, 0): "O", (1, 1): "O", (1, 2): "O"})
        assert spel.minimax(0, True, max_depth=2) == -1

        # Een niet-terminale staat op diepte 0 met max_depth=0
        spel = _maak_bord({(0, 0): "X", (1, 0): "O"})
        assert spel.minimax(0, True, max_depth=0) == 0


# =============== find_best_move ===============


def test_find_best_move_wint():
    """find_best_move kiest een winnende zet als die er is."""
    with time_limit():
        spel = _maak_bord({(0, 0): "X", (0, 1): "X", (1, 0): "O"})
        zet = spel.find_best_move()
    assert zet is not None, "er moet een zet gekozen worden"
    assert zet == (0, 2), f"verwacht winnende zet (0,2), kreeg {zet}"


def test_find_best_move_blokkeert():
    """find_best_move blokkeert de tegenstander als die bijna wint."""
    with time_limit():
        spel = _maak_bord({(0, 0): "O", (0, 1): "O", (1, 0): "X"})
        zet = spel.find_best_move()
    assert zet is not None, "er moet een zet gekozen worden"
    assert zet == (0, 2), f"verwacht blokkerende zet (0,2), kreeg {zet}"
