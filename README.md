# Asset Price Simulation via Geometric Brownian Motion (GBM)

This project implements a Monte Carlo simulation in Python using the **Geometric Brownian Motion (GBM)** stochastic process to project potential future stock price paths.

### Mathematical Framework

The stochastic differential equation (SDE) governing the asset price behavior in the Black-Scholes framework is:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Where:
* $S_t$: Asset price at time $t$.
* $\mu$: Annualized expected return or drift coefficient.
* $\sigma$: Annualized asset volatility.
* $dt$: Time step increment.
* $dW_t$: Wiener process or standard Brownian motion increment, representing market randomness.

###Analytical Solution via Itô's Lemma

By applying Itô's calculus to the transform $f(S_t)=\ln(S_t)$ we obtain the esact analytical solution for the asset price at any time $t$:

$$S_t=S_0exp\left( \left(\mu-\frac{\sigma^2}{2}\right)t+\sigma W_t\right)$$

This analytical form is of fundamental importance for the MOnte Carlo simulation. Rather than approximating the SDE step-by-step (which introduces discretization bias), the simulation leverages this exact solution to generate unbiased random walks across discrete time intervals $\Delta t$:

$$S_{t+\Delta t}=S_t exp\left( \left(\mu-\frac{\sigma^2}{2}\right)\Delta t+\sigma\epsilon\sqrt{\Delta t}\right)$$

Where $\epsilon \sim \mathcal{N}(0,1)$ represents a standard normal random variable.

## Features

* **Vectorized Simulation**: Implemented using `numpy` vectorized calculations to optimize computational performance during Monte Carlo loops.
* **Data Visualization**: Includes multi-path trajectory plotting using `matplotlib`.
* **Statistical Analysis**: Computes key metrics such as terminal price distribution and percentiles to analyze risk scenarios.

## Installation and Dependencies

To run this simulation locally, you need Python 3 installed along with the required numerical and plotting libraries:

```bash
pip install numpy matplotlib
```
## Usage and Parameter Configuration

You can execute the simulation script directly from your terminal:

```bash
python monte_carlo_gbm.py
```

The model variables can be adjusted directly inside the script to customize the simulation output:

```python
S0 = 100.0      # Initial stock price
mu = 0.05       # Annualized expected return (drift)
sigma = 0.20    # Annualized asset volatility
T = 1.0         # Time horizon in years
dt = 1/252      # Time step increment (e.g., daily intervals for a trading year)
n_paths = 1000  # Number of simulated price trajectories
```

## Expected Results

The simulation generates two primary outputs:

1. **Path Trajectories Plot**: Visualizes the simulated random walks of the asset over the specified time horizon $T$.
2. **Terminal Price Distribution**: Statistical breakdown displaying market risk expectations and potential final asset values.
















