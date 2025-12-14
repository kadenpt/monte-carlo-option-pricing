import numpy as np
import matplotlib.pyplot as plt

from src.gbm import simulate_gbm
from src.option_pricing import european_call_price
from src.sensitivity import volatility_sensitivity
from src.black_scholes import european_call_price_bs
from src.utils import calculate_confidence_interval

def validate_monte_carlo():
  np.random.seed(42)
  s0 = 100
  K = 100
  mu = 0.05
  sigma = 0.2
  r = 0.05
  T = 1.0

  steps = 252
  mu = r
  path_counts = [500, 1000, 2000, 5000, 10000, 25000, 50000]
  mc_prices = []

  bs_price = european_call_price_bs(s0, K, T, r, sigma)

  for n_paths in path_counts:
    paths = simulate_gbm(s0, mu, sigma, T, steps, n_paths)
    mc_price = european_call_price(paths, K, T, r)
    mc_prices.append(mc_price)

    print(f"Paths: {n_paths:>6} | MC Price: {mc_price:.4f} | BS Price: {bs_price:.4f} | Error: {mc_price - bs_price:+.4f}")

  plt.plot(path_counts, mc_prices, marker="o", label="Monte Carlo")
  plt.axhline(bs_price, linestyle="--", color="r", label="Black-Scholes")

  plt.xscale("log")
  plt.xlabel("Number of Paths")
  plt.ylabel("Option Price")
  plt.title("Monte Carlo vs. Black-Scholes")
  plt.legend()
  plt.savefig("plots/validate_monte_carlo.png")

def main():
  s0 = 100
  mu = 0.05
  sigma = 0.2
  r = 0.03
  T = 1.0
  steps = 100
  n_paths = 10000
  strike = 100

  paths = simulate_gbm(s0, mu, sigma, T, steps, n_paths)

  call_price = european_call_price(paths, strike, r, T)
  print(f"European call price: {call_price}")

  for i in range(50):
    plt.plot(paths[i])
  plt.title("Stock Price Paths")
  plt.xlabel("Time")
  plt.ylabel("Stock Price")
  plt.savefig("plots/stock_price_paths.png")

  vol_range = np.linspace(0.1, 0.6, 10)
  prices = volatility_sensitivity(vol_range, s0, mu, T, steps, n_paths, strike, r)
  plt.plot(vol_range, prices)
  plt.xlabel("Volatility")
  plt.ylabel("Price")
  plt.title("Volatility Sensitivity")
  plt.savefig("plots/volatility_sensitivity.png")

  low, high = calculate_confidence_interval(prices)
  print(f"Confidence interval: {low:.4f} - {high:.4f}")

if __name__ == "__main__":
  main()
  validate_monte_carlo()