import os, sys
from fastapi import FastAPI,HTTPException
from model import PortfolioInput,RiskMetricsOutput
from src_python.fetch_data import fetch_data
from src_python.analysis import calculate_parameters
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build')))
import riskengine

app = FastAPI()

@app.post("/portfolio/var",response_model=RiskMetricsOutput)
def calculate_var(req: PortfolioInput):
    try:
        print(f"Processing portfolio of size: {req.portfolio_size}")
        print(f"Analyzing tickers: {req.ticker}")

        data=fetch_data(req.ticker)

        mean_returns, cov_matrix = calculate_parameters(data)

        num_assets = len(req.tickers)
        weights = [1.0 / num_assets] * num_assets

        mean_flat = mean_returns.tolist()
        cov_flat = cov_matrix.flatten().tolist()

        engine = riskengine.MonteCarloEngine(num_assets, req.num_simulations)

        cpp_result = engine.runSimulation(
            req.portfolio_size, 
            weights, 
            mean_flat, 
            cov_flat
        )

        return RiskMetricsOutput(
            var_95=cpp_result.var95,
            var_99=cpp_result.var99,
            cvar=cpp_result.mean_loss,
            message="Simulation completed successfully via C++ engine."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    


