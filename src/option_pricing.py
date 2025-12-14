import numpy as np

def european_call_price(
  price_paths: np.ndarray,
  strike: float,
  r: float,
  T: float
) -> float:
  ST = price_paths[:, -1]
  payoffs = np.maximum(ST - strike, 0)
  discounted_payoffs = np.exp(-r * T) * np.mean(payoffs)
  return discounted_payoffs