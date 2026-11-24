"""
Week 9, deel B: kwadratische kost en 'dichtste bij'.

Test de publieke interface van de oplossing van de student:
- maaltijd_matrices: zet een kostenfunctie om naar P en q
- optimize_meal: berekent de optimale hoeveelheden per ingrediënt
- PortfolioOptimizer: minimaliseert het risico van een portefeuille
- verdeling_matrices / optimaliseer_verdeling: verdeling met 5 variabelen

De tests controleren enkel gedrag, niet hoe het geïmplementeerd is.
"""

import contextlib
import importlib
import threading

import numpy as np
import pytest

MODULE_PATH = "exercises.week09.solution"

try:
    _mod = importlib.import_module(MODULE_PATH)
    maaltijd_matrices = _mod.maaltijd_matrices
    optimize_meal = _mod.optimize_meal
    PortfolioOptimizer = _mod.PortfolioOptimizer
    verdeling_matrices = _mod.verdeling_matrices
    optimaliseer_verdeling = _mod.optimaliseer_verdeling
except Exception as import_error:
    pytest.skip(
        f"solution.py kon niet geïmporteerd worden: {import_error}",
        allow_module_level=True,
    )

WEIGHTS = {
    "test_maaltijd_matrices_P": 2,
    "test_maaltijd_matrices_q": 2,
    "test_optimize_meal_vorm": 1,
    "test_optimize_meal_som": 2,
    "test_optimize_meal_grenzen": 2,
    "test_portfolio_vorm": 1,
    "test_portfolio_som": 2,
    "test_portfolio_bereik": 2,
    "test_portfolio_deterministisch": 1,
    "test_portfolio_gelijkgewicht_diagonaal": 2,
    "test_verdeling_matrices_P": 1,
    "test_verdeling_matrices_q": 1,
    "test_optimaliseer_verdeling_vorm": 1,
    "test_optimaliseer_verdeling_resultaat": 2,
    "test_optimaliseer_verdeling_som": 2,
    "test_optimaliseer_verdeling_grenzen": 2,
}


@contextlib.contextmanager
def time_limit(seconds: int = 10):
    """Beperk de duur van een blok code (tegen infinite loops)."""
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


NUTRIENTEN = np.array([[2.8, 29, 2], [7, 0, 17], [0.4, 7, 0.1]])
DOELEN = np.array([37, 41, 20])
GRENZEN = [(2.0, 3.0), (1.0, 2.0), (2.0, 4.0)]


# --- Oefening 4: Macronutriënten ---


def test_maaltijd_matrices_P():
    """De kwadratische matrix P komt overeen met 2 * N.T @ N en is positief semidefiniet."""
    with time_limit():
        P, _ = maaltijd_matrices(NUTRIENTEN, DOELEN)
    verwacht = 2.0 * (NUTRIENTEN.T @ NUTRIENTEN)
    assert np.allclose(P, verwacht, atol=1e-9), (
        "P wijkt af van de verwachte kwadratische matrix"
    )
    eigen = np.linalg.eigvalsh(P)
    assert float(eigen[0]) >= -1e-9, (
        "P is positief semidefiniet"
    )


def test_maaltijd_matrices_q():
    """De lineaire vector q komt overeen met -2 * N.T @ doelen."""
    with time_limit():
        _, q = maaltijd_matrices(NUTRIENTEN, DOELEN)
    verwacht = -2.0 * (NUTRIENTEN.T @ DOELEN)
    assert np.allclose(q, verwacht, atol=1e-9), (
        "q wijkt af van de verwachte lineaire vector"
    )


def test_optimize_meal_vorm():
    """optimize_meal geeft één waarde per ingrediënt."""
    with time_limit():
        x = optimize_meal(NUTRIENTEN, DOELEN, GRENZEN)
    assert x is not None, "optimize_meal mag None niet teruggeven"
    assert len(x) == 3, f"er zijn 3 ingrediënten, kreeg {len(x)}"
    for waarde in x:
        assert np.isfinite(float(waarde)), "de oplossing bevat geldige getallen"


def test_optimize_meal_som():
    """De totale hoeveelheid blijft behouden (gelijkheid)."""
    with time_limit():
        x = optimize_meal(NUTRIENTEN, DOELEN, GRENZEN)
    som = float(np.sum(x))
    assert abs(som - 7.0) < 1e-2, (
        f"de totale som is {som:.4f}, verwacht 7.0"
    )


def test_optimize_meal_grenzen():
    """Elke hoeveelheid ligt binnen zijn opgegeven grenzen."""
    with time_limit():
        x = optimize_meal(NUTRIENTEN, DOELEN, GRENZEN)
    for i, (min_grens, max_grens) in enumerate(GRENZEN):
        assert float(x[i]) >= min_grens - 1e-2, (
            f"ingrediënt {i} ligt onder de ondergrens {min_grens}"
        )
        assert float(x[i]) <= max_grens + 1e-2, (
            f"ingrediënt {i} ligt boven de bovengrens {max_grens}"
        )


# --- Oefening 5: Portefeuille-optimalisatie ---


def test_portfolio_vorm():
    """fit geeft één gewicht per asset."""
    cov = np.array([[0.001, 0.0002, 0.0001],
                    [0.0002, 0.002, 0.0003],
                    [0.0001, 0.0003, 0.001]])
    with time_limit():
        w = PortfolioOptimizer([0.05, 0.08, 0.1], cov).fit()
    assert w is not None, "fit mag None niet teruggeven"
    assert len(w) == 3, f"er zijn 3 assets, kreeg {len(w)}"
    for waarde in w:
        assert np.isfinite(float(waarde)), "de gewichten zijn geldige getallen"


def test_portfolio_som():
    """De gewichten sommeren tot 1 (alles is belegd)."""
    cov = np.array([[0.001, 0.0002, 0.0001],
                    [0.0002, 0.002, 0.0003],
                    [0.0001, 0.0003, 0.001]])
    with time_limit():
        w = PortfolioOptimizer([0.05, 0.08, 0.1], cov).fit()
    som = float(np.sum(w))
    assert abs(som - 1.0) < 1e-3, f"de som van de gewichten is {som:.4f}"


def test_portfolio_bereik():
    """Elk gewicht ligt tussen 0 en 1."""
    cov = np.array([[0.001, 0.0002, 0.0001],
                    [0.0002, 0.002, 0.0003],
                    [0.0001, 0.0003, 0.001]])
    with time_limit():
        w = PortfolioOptimizer([0.05, 0.08, 0.1], cov).fit()
    for waarde in w:
        assert float(waarde) >= -1e-4, "een gewicht is niet negatief"
        assert float(waarde) <= 1.0 + 1e-4, "een gewicht is niet groter dan 1"


def test_portfolio_deterministisch():
    """Dezelfde portefeuille geeft dezelfde oplossing."""
    cov = np.array([[0.001, 0.0002, 0.0001],
                    [0.0002, 0.002, 0.0003],
                    [0.0001, 0.0003, 0.001]])
    optimizer = PortfolioOptimizer([0.05, 0.08, 0.1], cov)
    with time_limit():
        w1 = optimizer.fit()
        w2 = optimizer.fit()
    assert np.allclose(w1, w2, atol=1e-9), (
        "herhaalde fit geeft hetzelfde resultaat"
    )


def test_portfolio_gelijkgewicht_diagonaal():
    """Met een diagonaal covariantiematrix krijgt elke asset hetzelfde gewicht."""
    cov = np.identity(3) * 0.01
    with time_limit():
        w = PortfolioOptimizer([0.05, 0.08, 0.1], cov).fit()
    for waarde in w:
        assert abs(float(waarde) - 1.0 / 3.0) < 1e-3, (
            "symmetrisch probleem geeft gelijke gewichten"
        )


# --- Oefening 6: Trainingstijd (5 variabelen) ---

DOELEN_6 = np.array([8, 6, 5, 6, 5])
GRENZEN_6 = [(0.0, 10.0)] * 5


def test_verdeling_matrices_P():
    """P is 2 * I, want elke afstand tot een doel telt apart."""
    with time_limit():
        P, _ = verdeling_matrices(DOELEN_6)
    verwacht = 2.0 * np.identity(5)
    assert np.allclose(P, verwacht, atol=1e-9), (
        "P wijkt af van 2 * I voor een verdeling met losse doelen"
    )


def test_verdeling_matrices_q():
    """q is -2 * doelen."""
    with time_limit():
        _, q = verdeling_matrices(DOELEN_6)
    verwacht = -2.0 * DOELEN_6
    assert np.allclose(q, verwacht, atol=1e-9), (
        "q wijkt af van -2 * doelen"
    )


def test_optimaliseer_verdeling_vorm():
    """optimaliseer_verdeling geeft één waarde per variabele (hier 5)."""
    with time_limit():
        x = optimaliseer_verdeling(DOELEN_6, GRENZEN_6, 25.0)
    assert x is not None, "optimaliseer_verdeling mag None niet teruggeven"
    assert len(x) == 5, f"er zijn 5 disciplines, kreeg {len(x)}"
    for waarde in x:
        assert np.isfinite(float(waarde)), "de oplossing bevat geldige getallen"


def test_optimaliseer_verdeling_resultaat():
    """Het tekort van 5 uur wordt evenredig verdeeld over de 5 disciplines."""
    with time_limit():
        x = optimaliseer_verdeling(DOELEN_6, GRENZEN_6, 25.0)
    verwacht = np.array([7, 5, 4, 5, 4])
    assert np.allclose(x, verwacht, atol=1e-2), (
        "de optimale verdeling is [7, 5, 4, 5, 4]"
    )


def test_optimaliseer_verdeling_som():
    """De totale som blijft behouden (gelijkheid)."""
    with time_limit():
        x = optimaliseer_verdeling(DOELEN_6, GRENZEN_6, 25.0)
    som = float(np.sum(x))
    assert abs(som - 25.0) < 1e-2, (
        f"de totale som is {som:.4f}, verwacht 25.0"
    )


def test_optimaliseer_verdeling_grenzen():
    """Elke discipline ligt binnen zijn opgegeven grenzen."""
    with time_limit():
        x = optimaliseer_verdeling(DOELEN_6, GRENZEN_6, 25.0)
    for i, (min_grens, max_grens) in enumerate(GRENZEN_6):
        assert float(x[i]) >= min_grens - 1e-2, (
            f"discipline {i} ligt onder de ondergrens {min_grens}"
        )
        assert float(x[i]) <= max_grens + 1e-2, (
            f"discipline {i} ligt boven de bovengrens {max_grens}"
        )
