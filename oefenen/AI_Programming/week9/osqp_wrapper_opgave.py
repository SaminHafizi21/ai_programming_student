#todo
import numpy as np
import osqp
from scipy.sparse import csc_matrix

class PortfolioOptimizer:
    def __init__(self, expected_returns, covariance_matrix):
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)
        self.num_assets = len(expected_returns)
        self.alpha = 0.1

    def fit(self):
        pass

# Example usage:
if __name__ == "__main__":
    # Voorbeeldje
    expected_returns = [0.05, 0.08, 0.1]
    covariance_matrix = np.array([[0.001, 0.0002, 0.0001],
                                  [0.0002, 0.002, 0.0003],
                                  [0.0001, 0.0003, 0.001]])

    # initialisatie, fit PortfolioOptimizer
    optimizer = PortfolioOptimizer(expected_returns, covariance_matrix)
    optimal_weights = optimizer.fit()

    # Print 
    print("Optimale oplossing:")
    print(optimal_weights)
