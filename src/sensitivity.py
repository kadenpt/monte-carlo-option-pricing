import numpy as np
from src.gbm import simulate_gbm
from src.option_pricing import european_call_price

def volatility_sensitivity(
  vol_range,
  s0,
  mu,
  T,
  steps,
  n_paths,
  strike,
  r
) -> np.ndarray:
  prices = []
  for sigma in vol_range:
    price_paths = simulate_gbm(s0, mu, sigma, T, steps, n_paths)
    price = european_call_price(price_paths, strike, r, T)
    prices.append(price)
  return np.array(prices)