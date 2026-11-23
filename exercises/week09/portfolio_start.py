"""
Oefening 3: Portefeuille-optimalisatie ('dichtste bij')
=========================================================
"""
import numpy as np
import osqp
from scipy.sparse import csc_matrix


class PortfolioOptimizer:
    """Minimaliseer het risico van een portefeuille met OSQP."""

    def __init__(self, expected_returns, covariance_matrix):
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)
        self.num_assets = len(expected_returns)

    def fit(self):
        """Bereken de optimale gewichten van de portefeuille.

        Minimaliseer w.T @ cov @ w (risico) met als randvoorwaarden
        som(w) = 1 en 0 <= w_i <= 1.

        Returns:
            np.ndarray: de optimale gewichten w.
        """
        # TODO: stel P, q, A, l, u op en los op met OSQP.
        # P = 2 * cov, q = nul, A = [rij van enen; eenheidsmatrix].
        raise NotImplementedError


if __name__ == "__main__":
    expected_returns = [0.05, 0.08, 0.1]
    covariance_matrix = np.array([[0.001, 0.0002, 0.0001],
                                  [0.0002, 0.002, 0.0003],
                                  [0.0001, 0.0003, 0.001]])

    optimizer = PortfolioOptimizer(expected_returns, covariance_matrix)
    optimal_weights = optimizer.fit()
    print("Optimale gewichten:", np.round(optimal_weights, 3))