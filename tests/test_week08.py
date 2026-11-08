"""
Week 08 Autograder: Mini Othello met Minimax & Monty Hall.

Test de publieke interface van de oplossing van de student:
- Othello: __init__, is_valid_move, make_move, opponent, count_pieces,
  valid_moves, random_move, evaluate, minimax, best_move
- MontyHallGame: choose_door, host_reveal, switch_choice,
  is_player_winner, play_game
- expectimax_simulation

De tests controleren enkel gedrag, niet hoe het geïmplementeerd is.
Studentencode die crasht of infinite loopt wordt netjes afgehandeld.
"""

import contextlib
import importlib
import random
import threading

import pytest

MODULE_PATH = "exercises.week08.solution"

try:
    _mod = importlib.import_module(MODULE_PATH)
    Othello = _mod.Othello
    MontyHallGame = _mod.MontyHallGame
    expectimax_simulation = _mod.expectimax_simulation
except Exception as import_error:
    pytest.skip(
        f"solution.py kon niet geïmporteerd worden: {import_error}",
        allow_module_level=True,
    )

WEIGHTS = {
    "test_bord_init": 1,
    "test_is_valid_move": 1,
    "test_make_move": 1,
    "test_opponent": 1,
    "test_count_pieces": 1,
    "test_valid_moves_start": 1,
    "test_random_move": 2,
    "test_evaluate": 2,
    "test_minimax_diepte_0": 1,
    "test_minimax_simuleert_zetten": 2,
    "test_best_move": 2,
    "test_montyhall_kies_deur": 1,
    "test_montyhall_host_onthult_geit": 1,
    "test_montyhall_switch_kiest_resterende_deur": 1,
    "test_montyhall_winnaar": 1,
    "test_montyhall_play_game": 1,
    "test_montyhall_winrate_switch": 2,
    "test_montyhall_winrate_geen_switch": 2,
}


@contextlib.contextmanager
def time_limit(seconds: int = 10):
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


# =============== Othello: bord-initialisatie ===============


def test_bord_init():
    """Het bord is 8x8 met de startpositie (O op 3,3/4,4; X op 3,4/4,3)."""
    spel = Othello()
    with time_limit():
        assert len(spel.board) == 8, "bord moet 8 rijen hebben"
        for rij in spel.board:
            assert len(rij) == 8, "elke rij moet 8 kolommen hebben"

        assert spel.board[3][3] == "O"
        assert spel.board[4][4] == "O"
        assert spel.board[3][4] == "X"
        assert spel.board[4][3] == "X"

        for r in range(8):
            for c in range(8):
                if (r, c) in [(3, 3), (4, 4), (3, 4), (4, 3)]:
                    continue
                assert spel.board[r][c] == " ", f"veld ({r},{c}) moet leeg zijn"


# =============== Othello: is_valid_move ===============


def test_is_valid_move():
    """is_valid_move keurt ongeldige zetten af en geldige goed."""
    spel = Othello()
    with time_limit():
        # Geldige zetten voor X
        assert spel.is_valid_move(2, 3, "X") is True
        assert spel.is_valid_move(3, 2, "X") is True
        assert spel.is_valid_move(4, 5, "X") is True
        assert spel.is_valid_move(5, 4, "X") is True

        # Geldige zetten voor O
        assert spel.is_valid_move(2, 4, "O") is True
        assert spel.is_valid_move(3, 5, "O") is True
        assert spel.is_valid_move(4, 2, "O") is True
        assert spel.is_valid_move(5, 3, "O") is True

        # Ongeldig: bezet veld, buiten bereik, geen flankering
        assert spel.is_valid_move(3, 3, "X") is False  # bezet
        assert spel.is_valid_move(0, 0, "X") is False  # geen flankering
        assert spel.is_valid_move(-1, 0, "X") is False
        assert spel.is_valid_move(8, 0, "X") is False


# =============== Othello: make_move ===============


def test_make_move():
    """make_move plaatst een steen en draait de juiste stenen om."""
    spel = Othello()
    with time_limit():
        spel.make_move(2, 3, "X")
        assert spel.board[2][3] == "X"
        assert spel.board[3][3] == "X", "steen op (3,3) moet omgedraaid zijn"
        assert spel.board[4][4] == "O"
        assert spel.board[3][4] == "X"
        assert spel.board[4][3] == "X"


# =============== Othello: opponent en count_pieces ===============


def test_opponent():
    """opponent geeft de juiste tegenstander."""
    spel = Othello()
    with time_limit():
        spel.player = "X"
        assert spel.opponent() == "O"
        spel.player = "O"
        assert spel.opponent() == "X"


def test_count_pieces():
    """count_pieces geeft de correcte aantallen."""
    spel = Othello()
    with time_limit():
        x, o = spel.count_pieces()
        assert x == 2, f"start X = 2, kreeg {x}"
        assert o == 2, f"start O = 2, kreeg {o}"


# =============== Othello: valid_moves en random_move ===============


def test_valid_moves_start():
    """valid_moves geeft 4 geldige zetten voor X en 4 voor O op startbord."""
    spel = Othello()
    with time_limit():
        x_zetten = spel.valid_moves("X")
        assert len(x_zetten) == 4, (
            f"X moet 4 geldige zetten hebben, kreeg {len(x_zetten)}"
        )
        for zet in x_zetten:
            assert spel.is_valid_move(zet[0], zet[1], "X") is True

        o_zetten = spel.valid_moves("O")
        assert len(o_zetten) == 4, (
            f"O moet 4 geldige zetten hebben, kreeg {len(o_zetten)}"
        )


def test_random_move():
    """random_move geeft een geldige zet terug."""
    spel = Othello()
    with time_limit():
        for _ in range(10):
            zet = spel.random_move()
            assert zet is not None, "random_move mag None niet teruggeven"
            assert len(zet) == 2, (
                f"random_move moet (rij, kol) tuple geven, kreeg {zet}"
            )
            r, c = zet
            assert 0 <= r < 8 and 0 <= c < 8, f"zet ({r},{c}) is buiten het bord"
            assert spel.is_valid_move(r, c, "X") is True, (
                f"random_move gaf ongeldige zet ({r},{c})"
            )


# =============== Othello: evaluate ===============


def test_evaluate():
    """evaluate geeft een numerieke score terug voor een speler."""
    spel = Othello()
    with time_limit():
        score_x = spel.evaluate("X")
        score_o = spel.evaluate("O")
        assert isinstance(score_x, (int, float)), "evaluate moet een getal geven"
        assert isinstance(score_o, (int, float)), "evaluate moet een getal geven"

        # Na een sterke X-zet stijgt de X-score
        score_voor = spel.evaluate("X")
        spel.make_move(2, 3, "X")
        score_na = spel.evaluate("X")
        assert score_na > score_voor, "evaluate moet een verbetering zien na een zet"


# =============== Othello: minimax en best_move ===============


def test_minimax_diepte_0():
    """minimax met depth=0 geeft de evaluate-score terug."""
    spel = Othello()
    with time_limit():
        score = spel.minimax(0, True, "X")
        assert score == spel.evaluate("X")

        score = spel.minimax(0, True, "O")
        assert score == spel.evaluate("O")


def test_minimax_simuleert_zetten():
    """minimax simuleert zetten en wijzigt het bord niet permanent."""
    spel = Othello()
    with time_limit():
        bord_voor = [rij[:] for rij in spel.board]

        score = spel.minimax(2, True, "X")

        for r in range(8):
            for c in range(8):
                assert spel.board[r][c] == bord_voor[r][c], (
                    f"minimax mag het bord niet wijzigen, veld ({r},{c}) veranderd"
                )
        assert isinstance(score, (int, float)), "minimax moet een getal geven"


def test_best_move():
    """best_move geeft een geldige zet terug en wijzigt het bord niet."""
    spel = Othello()
    with time_limit():
        bord_voor = [rij[:] for rij in spel.board]
        zet = spel.best_move()
        assert zet is not None, "best_move mag None niet teruggeven"
        assert len(zet) == 2, f"best_move moet (rij, kol) tuple geven, kreeg {zet}"
        r, c = zet
        assert 0 <= r < 8 and 0 <= c < 8, f"zet ({r},{c}) is buiten het bord"
        assert spel.is_valid_move(r, c, "X") is True, (
            f"best_move gaf ongeldige zet ({r},{c}) voor X"
        )
        for r0 in range(8):
            for c0 in range(8):
                assert spel.board[r0][c0] == bord_voor[r0][c0], (
                    "best_move mag het bord niet wijzigen"
                )

# =============== Monty Hall ===============


def test_montyhall_kies_deur():
    """choose_door aanvaardt 0-2 en verwerpt ongeldige deurnummers."""
    spel = MontyHallGame()
    with time_limit():
        spel.choose_door(0)
        assert spel.player_choice == 0
        spel.choose_door(2)
        assert spel.player_choice == 2
        spel.choose_door(3)  # ongeldig: vorige keuze blijft bewaard
        assert spel.player_choice == 2


def test_montyhall_host_onthult_geit():
    """host_reveal onthult altijd een deur met een geit, niet de keuze."""
    with time_limit():
        for _ in range(30):
            spel = MontyHallGame()
            spel.choose_door(random.randrange(3))
            spel.host_reveal()
            assert spel.host_reveals is not None, "host moet een deur onthullen"
            assert spel.host_reveals != spel.player_choice, (
                "host mag de spelerkeuze niet onthullen"
            )
            assert spel.doors[spel.host_reveals] == "geit", (
                "host moet een geit onthullen"
            )


def test_montyhall_switch_kiest_resterende_deur():
    """switch_choice wisselt naar de enige overblijvende dichte deur."""
    with time_limit():
        for _ in range(30):
            spel = MontyHallGame()
            spel.choose_door(random.randrange(3))
            oude_keuze = spel.player_choice
            spel.host_reveal()
            assert spel.host_reveals is not None
            assert oude_keuze is not None
            spel.switch_choice()
            assert spel.player_choice is not None
            assert spel.player_choice != oude_keuze, "speler moet wisselen"
            assert spel.player_choice != spel.host_reveals, (
                "speler mag geen onthulde deur kiezen"
            )


def test_montyhall_winnaar():
    """is_player_winner klopt: alleen 'auto' achter de keuze wint."""
    with time_limit():
        for _ in range(10):
            spel = MontyHallGame()
            auto_deur = spel.doors.index("auto")
            spel.choose_door(auto_deur)
            assert spel.is_player_winner() is True

            spel2 = MontyHallGame()
            geit_deur = spel2.doors.index("geit")
            spel2.choose_door(geit_deur)
            assert spel2.is_player_winner() is False


def test_montyhall_play_game():
    """play_game speelt een volledig spel en geeft een bool terug."""
    with time_limit():
        for _ in range(20):
            spel = MontyHallGame()
            resultaat = spel.play_game(switch=True)
            assert isinstance(resultaat, bool), "play_game moet een bool geven"
            assert resultaat == spel.is_player_winner()


def test_montyhall_winrate_switch():
    """Met wisselen wint de speler in ongeveer 2/3 van de spellen."""
    with time_limit(20):
        winrate = expectimax_simulation(switch=True, num_simulations=5000)
    assert 2 / 3 - 0.06 < winrate < 2 / 3 + 0.06, (
        f"verwacht een winrate rond 2/3, kreeg {winrate:.4f}"
    )


def test_montyhall_winrate_geen_switch():
    """Zonder wisselen wint de speler in ongeveer 1/3 van de spellen."""
    with time_limit(20):
        winrate = expectimax_simulation(switch=False, num_simulations=5000)
    assert 1 / 3 - 0.06 < winrate < 1 / 3 + 0.06, (
        f"verwacht een winrate rond 1/3, kreeg {winrate:.4f}"
    )

