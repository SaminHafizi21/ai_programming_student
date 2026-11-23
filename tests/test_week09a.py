"""
Week 9, deel A: lineair programmeren met OSQP.

Test de publieke interface van de oplossing van de student:
- solve_qp: lost een kwadratisch probleem op
- solve_linear: zet een bovenlimiet-probleem om naar OSQP-vorm
- FabriekOptimizer: berekent het optimale productieplan

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
    solve_qp = _mod.solve_qp
    solve_linear = _mod.solve_linear
    FabriekOptimizer = _mod.FabriekOptimizer
except Exception as import_error:
    pytest.skip(
        f"solution.py kon niet geïmporteerd worden: {import_error}",
        allow_module_level=True,
    )

WEIGHTS = {
    "test_solve_qp_vorm": 1,
    "test_solve_qp_voldoet_constraints": 2,
    "test_solve_linear_optimum": 2,
    "test_solve_linear_infeasible": 1,
    "test_fabriek_optimale_productie": 2,
    "test_fabriek_constraints": 2,
    "test_fabriek_parameters": 1,
    "test_fabriek_attributen": 1,
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


# --- Oefening 1: OSQP basis ---


def test_solve_qp_vorm():
    """solve_qp geeft een numerieke vector met evenveel waarden als variabelen."""
    P = np.array([[4, 1], [1, 2]])
    q = np.array([1, 1])
    A = np.array([[1, 1], [-1, 2], [2, 1]])
    l = np.array([1, 0, 2])
    u = np.array([2, 2, 3])
    with time_limit():
        x = solve_qp(P, q, A, l, u)
    assert x is not None, "solve_qp mag None niet teruggeven"
    assert len(x) == 2, f"er zijn 2 variabelen, kreeg {len(x)}"
    for waarde in x:
        assert np.isfinite(float(waarde)), "de oplossing bevat geldige getallen"


def test_solve_qp_voldoet_constraints():
    """De oplossing voldoet aan de randvoorwaarden l <= A x <= u."""
    P = np.array([[4, 1], [1, 2]])
    q = np.array([1, 1])
    A = np.array([[1, 1], [-1, 2], [2, 1]])
    l = np.array([1, 0, 2])
    u = np.array([2, 2, 3])
    with time_limit():
        x = solve_qp(P, q, A, l, u)
    Ax = A @ x
    for i in range(len(l)):
        assert float(Ax[i]) >= l[i] - 1e-2, (
            f"randvoorwaarde {i}: {Ax[i]:.4f} ligt onder de ondergrens {l[i]}"
        )
        assert float(Ax[i]) <= u[i] + 1e-2, (
            f"randvoorwaarde {i}: {Ax[i]:.4f} ligt boven de bovengrens {u[i]}"
        )


# --- Oefening 2: Gx <= h omzetten ---


def test_solve_linear_optimum():
    """solve_linear maximaliseert de som met c = [-1, -1] en één bovenlimiet."""
    c = np.array([-1.0, -1.0])
    G = np.array([[1.0, 1.0]])
    h = np.array([10.0])
    with time_limit():
        x = solve_linear(c, G, h)
    assert x is not None, "solve_linear mag None niet teruggeven"
    som = float(np.sum(x))
    assert abs(som - 10.0) < 1e-3, (
        f"de som van de variabelen is {som:.4f}, verwacht 10.0"
    )
    for waarde in x:
        assert float(waarde) >= -1e-4, (
            "de variabelen mogen niet negatief zijn"
        )
    assert float(np.asarray(G @ x).reshape(-1)[0]) <= h[0] + 1e-3, (
        "de bovengrens omgekeerd in de oplossing"
    )


def test_solve_linear_infeasible():
    """Bij een onoplosbaar probleem geeft solve_linear None terug."""
    c = np.array([1.0])
    G = np.array([[1.0]])
    h = np.array([-1.0])
    with time_limit():
        x = solve_linear(c, G, h)
    assert x is None, (
        "een probleem zonder oplossing geeft None terug"
    )


# --- Oefening 3: Fabrieksoptimalisatie ---


def test_fabriek_optimale_productie():
    """Met de standaardvoorraden is het optimum ongeveer (42, 16)."""
    with time_limit():
        a, b = FabriekOptimizer().optimize()
    assert abs(a - 42.0) < 0.5, f"aantal AquaSparkles is {a:.2f}, verwacht ~42"
    assert abs(b - 16.0) < 0.5, f"aantal BioBursts is {b:.2f}, verwacht ~16"


def test_fabriek_constraints():
    """De oplossing respecteert de voorraadbeperkingen."""
    optim = FabriekOptimizer().optimize()
    assert not isinstance(optim, (float, int)), (
        "optimize geeft het aantal producten terug"
    )
    a, b = optim
    assert 2.0 * a + b <= 100.0 + 2e-2, "beperking op grondstof X overtreden"
    assert a + 3.0 * b <= 90.0 + 2e-2, "beperking op grondstof Y overtreden"
    assert a >= -1e-2 and b >= -1e-2, "het aantal producten mag niet negatief zijn"


def test_fabriek_parameters():
    """Aangepaste voorraden leiden tot een ander productieplan."""
    optim_default = FabriekOptimizer().optimize()
    optim_ruim = FabriekOptimizer(x_limit=200.0, y_limit=200.0).optimize()
    a_ruim = float(np.sum(optim_ruim))
    a_default = float(np.sum(optim_default))
    assert a_ruim > a_default, (
        "een grotere voorraad laat een grotere productie toe"
    )


def test_fabriek_attributen():
    """De parameters worden bij initialisatie opgeslagen."""
    fabriek = FabriekOptimizer(x_limit=50.0, y_limit=45.0, profit_a=3.0, profit_b=9.0)
    assert fabriek.x_limit == 50.0, "x_limit wordt opgeslagen"
    assert fabriek.y_limit == 45.0, "y_limit wordt opgeslagen"
    assert fabriek.profit_a == 3.0, "profit_a wordt opgeslagen"
    assert fabriek.profit_b == 9.0, "profit_b wordt opgeslagen"
