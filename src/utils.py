import numpy as np
from scipy.stats import norm

def calculate_confidence_interval(
  prices: np.ndarray,
  confidence: float = 0.95
) -> tuple[float, float]:
  n = len(prices)
  mean = np.mean(prices)
  std = np.std(prices)
  z = norm.ppf(1 - (1 - confidence) / 2)
  margin_of_error = z * (std / np.sqrt(n))
  return mean - margin_of_error, mean + margin_of_error