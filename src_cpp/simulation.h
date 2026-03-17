#ifndef SIMULATION_H
#define SIMULATION_H

#include <vector>

struct SimResult 
{
    double var95;
    double var99;
    double mean_loss;
};

class MonteCarloEngine 
{
private:
    int assets;
    int sim;

public:
    MonteCarloEngine(int assets, int sim);
    ~MonteCarloEngine();

    SimResult runSimulation(
        double initial_portfolio_value,
        const std::vector<double>& weights,
        const std::vector<double>& mean_returns,
        const std::vector<double>& cov_matrix 
    );
};

#endif