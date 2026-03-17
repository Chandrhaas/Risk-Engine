import sys
import os
import numpy as np
import pandas as pd  

current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(current_dir, '..', 'build')
# Point Python to your compiled C++ library
sys.path.append('./build')
import riskengine 

def main():
    print("--- Starting Risk Engine ---")
    
    # Define where our data lives
    means_file = "data/means.csv"
    cov_file = "data/covariance.csv"
    
    if not os.path.exists(means_file) or not os.path.exists(cov_file):
        print("Error: Parameter files not found. Please run your analysis.py first")
        return

    print("Loading real market data...")
    
    # Load the data using Pandas
    means_df = pd.read_csv(means_file, index_col=0)
    cov_df = pd.read_csv(cov_file, index_col=0)
    
    # determine the parameters
    assets = len(means_df)
    sim = 10000
    initial_value = 10000.0
    
    print(f"Detected {assets} assets: {list(means_df.index)}")

    # Create an equally weighted portfolio 
    weights = np.full(assets, 1.0 / assets, dtype=np.float64)
    
    # Extract the values from pandas and convert to float64 arrays
    # .iloc[:, 0] grabs the first column of the means dataframe
    mean_returns = np.array(means_df.iloc[:, 0].values, dtype=np.float64)
    
    #Extract the 2D covariance matrix and flatten it to 1D
    cov_matrix = np.array(cov_df.values.flatten(), dtype=np.float64)

    print("Initializing C++ Monte Carlo Engine...")
    engine = riskengine.MonteCarloEngine(assets, sim)
    
    print(f"Running {sim} simulations in C++...")
    result = engine.runSimulation(initial_value, weights, mean_returns, cov_matrix)
    
    print("\n--- RESULTS ---")
    print(f"95% Value at Risk (VaR): ${result.var95:.2f}")
    print(f"99% Value at Risk (VaR): ${result.var99:.2f}")
    print(f"95% Expected Shortfall : ${result.mean_loss:.2f}")

if __name__ == "__main__":
    main()