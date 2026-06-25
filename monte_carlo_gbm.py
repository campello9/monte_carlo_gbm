# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:15:40 2026

@author: Hector Campello
"""

#=============================================================================
#Monte Carlo Simulation for Geometric Brownian Motion in a Stock Price
#=============================================================================


#Imagine a stock  is worth $100 today. 
#We want to simulate 1000 possible scenarios of how this stock will behave
#over the next 252 business trading days.
#We assume the stock has an expected annual return of 10% (mu=0.10)
#and an annual volatility of 20% (sigma=0.20)

import numpy as np
import matplotlib.pyplot as plt

#Import necessary libraries for the exercise

np.random.seed(42)

#We fix a random seed (42 is just a convention, it could be any number).
#With this we ensure the plot is always reproducible: the random matrix
#will generate the exact same numbers every time the script runs, so they are
#random but consistent across runs.

S0=100 #Initial stock price
mu=0.10 #Expected return
sigma=0.2 #Volatility
T=1 #One year
num_simul=1000 #Number of scenarios to simulate
N=252 #Trading days in a year
mean=0 #Mean of the standard normal distribution
desv=1 #Standard deviation of the standard normal distribution

#Set up the necessary model variables

M=np.zeros((N+1,num_simul))


#Create an empty matrix to store the simulation results.
#This matrix has N+1 rows to include the initial price S0 at day 0.
#We construct a matrix with the number of simulations as columns
#and the number of days as rows. Each column represents a different scenario.

M[0,:]=S0

#Set the initial price for all scenarios in the first row of the matrix to S0.

dt=T/N

#Set the time step increment on annualized basis.

Z=np.random.normal(mean,desv,size=(N,num_simul))

#This matrix is filled with positive and negative random values from a normal distribution.
#If a number is positive, the stock price goes up; if negative, it goes down.
#Being a normal distribution, the highest density of events occurs around small absolute values
#(68% fall between -1 and 1, 95% between -2 and 2). This reflects that extreme jumps or drops
#are less likely. The matrix has N rows, as the first row of M is already fixed with S0.


#Pre-calculate constant terms outside the loop to optimize performance.
#The computer calculates this once instead of repeting it 252 times.

drift_total=(mu-1/2*sigma**2)*dt
volat_total=sigma*np.sqrt(dt)

for t in range (1,N+1):
    M[t]=M[t-1]*np.exp(drift_total+volat_total*Z[t-1])

#We populate matrix M using the analytical solution of the Stochastic Differential Equation
#derived from Itô's Lemma (Itô's Lemma is to stochastic differential equation what Taylor's
#Theorem is to standard calculus for finding analytical solutions), discretizing time
#via the Euler-Maruyama method.

plt.figure(figsize=(10,6))
plt.plot(M,lw=0.5)
plt.title(f'Monte Carlo Simulation: {num_simul} Scenarios for the Stock')
plt.xlabel('Trading Days (days)')
plt.ylabel('Stock Price ($)')
plt.grid(True) 
plt.show()

#The matrix of all 1000 paths is plotted. As expected, the vast majority of scenarios
#cluster around the center, and only a few suffer extreme drops or rises over the 252 days.

