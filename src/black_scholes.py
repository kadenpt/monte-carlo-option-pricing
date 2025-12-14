import numpy as np
from scipy.stats import norm

def european_call_price_bs(
  s0: float,
  K: float,
  T: float,
  r: float,
  sigma: float
) -> float:
  d1 = (np.log(s0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  d2 = d1 - sigma * np.sqrt(T)
  return s0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)