# Monte Carlo Option Pricing in Python

## Overview

This project implements **Monte Carlo simulations** to price financial options by modeling asset prices as stochastic processes. The primary objective is to understand how uncertainty, volatility, and time affect derivative pricing using **Geometric Brownian Motion (GBM)**.

The project provides a complete implementation including:
- **Monte Carlo simulation** for European call option pricing
- **Black-Scholes analytical pricing** for validation and comparison
- **Sensitivity analysis** to understand how volatility affects option prices
- **Visualization tools** for stock price paths and sensitivity analysis
- **Validation framework** comparing Monte Carlo convergence to Black-Scholes

The project is implemented in **vanilla Python**, focusing on clean code structure, modular design, and reproducibility outside of Jupyter notebooks.

---

## Key Features

- **Geometric Brownian Motion (GBM) Simulation**: Generate multiple asset price paths using stochastic differential equations
- **European Call Option Pricing**: Price options using Monte Carlo methods with configurable parameters
- **Black-Scholes Validation**: Compare Monte Carlo results against analytical Black-Scholes formula
- **Volatility Sensitivity Analysis**: Analyze how option prices change with varying volatility levels
- **Convergence Analysis**: Validate Monte Carlo accuracy by comparing results across different numbers of simulation paths
- **Statistical Tools**: Calculate confidence intervals for pricing estimates
- **Visualization**: Generate plots for stock price paths, volatility sensitivity, and validation results

---

## Key Concepts

- Stochastic processes  
- Geometric Brownian Motion (GBM)  
- Monte Carlo methods  
- European option pricing  
- Black-Scholes model
- Sensitivity analysis (volatility)
- Statistical convergence

---

## Mathematical Model

### Asset Price Dynamics

The underlying asset price \( S_t \) follows **Geometric Brownian Motion**:

\[
dS_t = \mu S_t dt + \sigma S_t dW_t
\]

In discrete time:

\[
S_{t+1} = S_t \cdot \exp\left((\mu - \tfrac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t} Z\right)
\]

Where:
- \( \mu \) is the drift (expected return)
- \( \sigma \) is the volatility  
- \( Z \sim \mathcal{N}(0,1) \)

### Option Pricing via Monte Carlo

For a **European call option**, the payoff at maturity is:

\[
\max(S_T - K, 0)
\]

The option price is computed as the discounted expected payoff:

\[
\text{Price} = e^{-rT} \cdot \mathbb{E}[\text{payoff}]
\]

Monte Carlo simulation approximates this expectation by:
1. Simulating many asset price paths  
2. Computing the payoff for each path  
3. Averaging the results  
4. Discounting to present value  

### Black-Scholes Analytical Formula

For comparison and validation, the project also implements the Black-Scholes analytical formula:

\[
C = S_0 \Phi(d_1) - Ke^{-rT} \Phi(d_2)
\]

where:
- \( d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \)
- \( d_2 = d_1 - \sigma\sqrt{T} \)
- \( \Phi \) is the cumulative distribution function of the standard normal distribution

---

## Project Structure

```text
monte-carlo-option-pricing/
│
├── src/
│   ├── gbm.py              # Geometric Brownian Motion simulation
│   ├── option_pricing.py   # Monte Carlo option pricing logic
│   ├── black_scholes.py    # Black-Scholes analytical pricing
│   ├── sensitivity.py      # Volatility sensitivity analysis
│   └── utils.py            # Statistical utilities (confidence intervals)
│
├── plots/                  # Generated visualization figures
│   ├── stock_price_paths.png
│   ├── volatility_sensitivity.png
│   └── validate_monte_carlo.png
│
├── main.py                 # Main entry point with examples
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main script to see examples of:
- Monte Carlo option pricing
- Stock price path visualization
- Volatility sensitivity analysis
- Validation against Black-Scholes

```bash
python main.py
```

This will:
1. Generate 10,000 stock price paths using GBM
2. Calculate the European call option price
3. Visualize sample stock price paths
4. Analyze volatility sensitivity
5. Validate Monte Carlo convergence against Black-Scholes

---

## Dependencies

- `numpy` - Numerical computations and array operations
- `matplotlib` - Plotting and visualization
- `scipy` - Statistical functions (normal distribution)

---

## Example Output

The project generates three types of visualizations:

1. **Stock Price Paths**: Sample trajectories of simulated asset prices
2. **Volatility Sensitivity**: How option prices vary with volatility
3. **Monte Carlo Validation**: Convergence of Monte Carlo prices to Black-Scholes as the number of paths increases
