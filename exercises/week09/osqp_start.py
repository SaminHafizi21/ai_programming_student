"""
Oefening 1: OSQP Basis
=======================
"""
import numpy as np
import osqp
from scipy.sparse import csc_matrix


def solve_qp(P, q, A, l, u):
    prob = osqp.OSQP()
    prob.setup(csc_matrix(P), q, csc_matrix(A), l, u)
    result = prob.solve()
    return result.x


POSITIEF = np.inf
NEGATIEF = -np.inf


def solve_linear(c, G, h):
    """Los een lineair probleem met bovenlimieten op.

    Minimaliseer c.T @ x met G @ x <= h en x >= 0.

    Parameters:
        c (array): lineaire kostvector.
        G (array): constraintmatrix voor de bovenlimieten.
        h (array): bovenlimieten van G @ x.

    Returns:
        np.ndarray: de optimale waarden van x.
    """
    # TODO: bouw P (nul-matrix), A (G + eenheidsmatrix) en de grenzen l, u.
    # Rijen van G: ondergrens -inf, bovengrens h.
    # Rijen van de eenheidsmatrix: ondergrens 0, bovengrens +inf.
    raise NotImplementedError


class FabriekOptimizer:
    """Optimaliseer het productieproces van twee producten."""

    def __init__(self, x_limit=100.0, y_limit=90.0, profit_a=5.0, profit_b=8.0):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.profit_a = profit_a
        self.profit_b = profit_b

    def optimize(self):
        """Bereken het aantal AquaSparkles en BioBursts met maximale winst.

        Returns:
            tuple: het aantal AquaSparkles en BioBursts.
        """
        # TODO: stel P, q, A, l, u op en los op met OSQP.
        # q = -profit (maximaliseren is tegengesteld minimaliseren).
        raise NotImplementedError


if __name__ == "__main__":
    example_P = np.array([[4, 1], [1, 2]])
    example_q = np.array([1, 1])
    example_A = np.array([[1, 1], [-1, 2], [2, 1]])
    example_l = np.array([1, 0, 2])
    example_u = np.array([2, 2, 3])

    x = solve_qp(example_P, example_q, example_A, example_l, example_u)
    print("Oefening 1:", np.round(x, 3))

    factory = FabriekOptimizer()
    a, b = factory.optimize()
    print(f"Oefening 3: a = {a:.1f}, b = {b:.1f}")