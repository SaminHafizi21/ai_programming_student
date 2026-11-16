"""
Week 08 Autograder: Mini Othello met Minimax & Monty Hall.

Test de publieke interface van de oplossing van de student:
- Othello: __init__, is_valid_move, make_move, opponent, count_pieces,
  valid_moves, random_move, evaluate, minimax, best_move
- MontyHallGame: choose_door, host_reveal, switch_choice,
  is_player_winner, play_game
- expectimax_simulation
- TicTacToe: make_move, evaluate, copy, minimax (expectimax met
  chance-knopen), find_best_move, random_move

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
    "test_tictactoe_bord_init": 1,
    "test_tictactoe_make_move": 1,
    "test_tictactoe_evaluate": 2,
    "test_tictactoe_copy": 1,
    "test_tictactoe_minimax_diepte_0": 1,
    "test_tictactoe_minimax_wint": 2,
    "test_tictactoe_minimax_wijzigt_bord_niet": 2,
    "test_tictactoe_find_best_move_wint": 2,
    "test_tictactoe_find_best_move_blokkeert": 2,
    "test_tictactoe_random_move_geldig": 1,
    "test_tictactoe_chance_gemiddelde": 3,
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


# =============== TicTacToe met Expectimax ===============


def test_tictactoe_bord_init():
    """TicTacToe start met een leeg 3x3-bord en X aan zet."""
    spel = TicTacToe()
    with time_limit():
        assert len(spel.board) == 3, "bord moet 3 rijen hebben"
        for rij in spel.board:
            assert len(rij) == 3, "elke rij moet 3 kolommen hebben"
            assert all(cel == " " for cel in rij), "bord moet leeg starten"
        assert spel.xTurn is True, "X moet beginnen"


def test_tictactoe_make_move():
    """make_move plaatst enkel op geldige, vrije velden en houdt de beurt bij."""
    spel = TicTacToe()
    with time_limit():
        assert spel.make_move(0, 0, "X") is True
        assert spel.board[0][0] == "X"
        assert spel.xTurn is False, "na X is O aan zet"

        # Verkeerde speler mag niet zetten
        assert spel.make_move(0, 1, "X") is False, "X is niet meer aan zet"
        # Bezet veld afgewezen
        assert spel.make_move(0, 0, "O") is False, "veld is bezet"
        # Buiten het bord
        assert spel.make_move(3, 0, "O") is False, "(3,0) is buiten het bord"


def test_tictactoe_evaluate():
    """evaluate geeft 1 (X wint), -1 (O wint) of 0 (geen winnaar)."""
    # Rij met drie X-en
    spel = TicTacToe()
    spel.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
    with time_limit():
        assert spel.evaluate() == 1, "drie X op een rij moet score 1 geven"

        # Kolom met drie O-en
        spel2 = TicTacToe()
        spel2.board = [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]]
        assert spel2.evaluate() == -1, "drie O op een rij moet score -1 geven"

        # Diagonaal met X
        spel3 = TicTacToe()
        spel3.board = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        assert spel3.evaluate() == 1, "diagonaal met X moet score 1 geven"

        # Geen winnaar
        spel4 = TicTacToe()
        assert spel4.evaluate() == 0, "leeg bord heeft score 0"


def test_tictactoe_copy():
    """copy maakt een onafhankelijke kopie van het spel."""
    spel = TicTacToe()
    spel.board[0][0] = "X"
    with time_limit():
        kopie = spel.copy()
        kopie.board[0][0] = "O"
        assert spel.board[0][0] == "X", "bord van het origineel mag niet wijzigen"
        assert kopie.board[0][0] == "O", "kopie krijgt eigen bord"


def test_tictactoe_minimax_diepte_0():
    """minimax met depth=0 geeft de evaluate-score terug."""
    spel = TicTacToe()
    with time_limit():
        assert spel.minimax(0, True) == 0
        assert spel.minimax(0, False) == 0


def test_tictactoe_minimax_wint():
    """minimax herkent een gewonnen staat voor X en geeft 1 terug."""
    spel = TicTacToe()
    spel.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
    with time_limit():
        assert spel.minimax(5, True) == 1, "X heeft gewonnen, score moet 1 zijn"
        assert spel.minimax(5, False) == 1, "terminal staat geeft 1"


def test_tictactoe_minimax_wijzigt_bord_niet():
    """minimax simuleert zetten op een kopie en wijzigt het bord niet."""
    spel = TicTacToe()
    with time_limit():
        bord_voor = [rij[:] for rij in spel.board]
        score = spel.minimax(6, True)
        assert isinstance(score, (int, float)), "minimax moet een getal geven"
        for r in range(3):
            for c in range(3):
                assert spel.board[r][c] == bord_voor[r][c], (
                    f"minimax mag het bord niet wijzigen, veld ({r},{c}) veranderd"
                )


def test_tictactoe_find_best_move_wint():
    """find_best_move kiest de zet waarmee X direct wint."""
    spel = TicTacToe()
    # X kan (0, 2) zetten en wint de bovenste rij
    spel.board = [["X", "X", " "], [" ", "O", " "], [" ", " ", " "]]
    with time_limit():
        zet = spel.find_best_move()
        assert zet == (0, 2), (
            f"verwacht winnende zet (0, 2), kreeg {zet}"
        )


def test_tictactoe_find_best_move_blokkeert():
    """find_best_move blokkeert een gereed liggende winnende zet van O."""
    spel = TicTacToe()
    # O dreigt rij 0 te winnen; X moet (0, 2) blokkeren om te verhinderen
    spel.board = [["O", "O", " "], ["X", " ", " "], [" ", " ", " "]]
    with time_limit():
        zet = spel.find_best_move()
        assert zet == (0, 2), (
            f"verwacht blokkerende zet (0, 2), kreeg {zet}"
        )


def test_tictactoe_random_move_geldig():
    """random_move geeft altijd een leeg veld binnen het bord terug."""
    spel = TicTacToe()
    with time_limit():
        for _ in range(20):
            zet = spel.random_move()
            assert len(zet) == 2, f"random_move moet (rij, kol) geven, kreeg {zet}"
            r, c = zet
            assert 0 <= r < 3 and 0 <= c < 3, f"zet ({r},{c}) is buiten het bord"
            assert spel.board[r][c] == " ", f"veld ({r},{c}) moet leeg zijn"


def test_tictactoe_chance_gemiddelde():
    """Een chance-knoop neemt het gemiddelde over alle willekeurige zetten.

    De waarde van een chance-knoop moet gelijk zijn aan het gemiddelde van
    de waarden van elke willekeurige zet van de tegenstander. We vergelijken
    ``minimax`` met ``is_chance=True`` tegen dat gemiddelde, berekend door
    elke O-zet afzonderlijk te bekijken. Een foute implementatie die op een
    chance-knoop ``min`` of ``max`` gebruikt in plaats van het gemiddelde
    zou deze test doen falen.
    """
    spel = TicTacToe()
    spel.board = [
        ["X", " ", "X"],
        [" ", "O", " "],
        [" ", " ", " "],
    ]

    with time_limit():
        kanswaarde = spel.minimax(6, False, is_chance=True)

        # Het gemiddelde over elke willekeurige O-zet op depth 5
        total = 0.0
        aantal = 0
        for r in range(3):
            for c in range(3):
                if spel.board[r][c] == " ":
                    kopie = spel.copy()
                    kopie.board[r][c] = "O"
                    total += kopie.minimax(5, True, is_chance=False)
                    aantal += 1
        verwacht = total / aantal

    assert aantal == 6, "er horen 6 lege velden te zijn voor O"
    assert kanswaarde == pytest.approx(verwacht, abs=1e-9), (
        "chance-knoop moet het gemiddelde over alle O-zetten nemen, "
        f"kreeg {kanswaarde}, verwacht {verwacht}"
    )

