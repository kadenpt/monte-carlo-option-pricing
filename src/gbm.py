import numpy as np

def simulate_gbm(
    s0: float,
    mu: float,
    sigma: float,
    T: float,
    steps: int,
    n_paths,
    seed: int = 42
) -> np.ndarray:
    dt = T / steps

    np.random.seed(seed)

    Z = np.random.normal(0, 1, size=(n_paths, steps))

    # Initialize the stock price paths
    S = np.zeros((n_paths, steps + 1))
    S[:, 0] = s0

    for t in range(1, steps + 1):
      S[:, t] = S[:, t - 1] * np.exp(
        (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[:, t - 1]
      )

    return S