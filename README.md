# Risk-Engine
I built a high-performance Monte Carlo Risk Engine. It is a quantitative finance tool that simulates thousands of potential future market paths to calculate critical portfolio risk metrics, specifically 95% Value at Risk (VaR) , 99% Value at Risk(VaR) and Expected Shortfall

# Technologies used
* c++
* python
    * Numpy
    * Pandas
    * yfinance
    * streamlit
    * pybind11

# Features
* Users can enter the stock tickers they want.
* Users can enter the number of simulations they want to run.
* Users can enter the size of the portfolio.

The Risk Engine applies Cholesky Decomposition to ensure simulated asset paths respect real-world market correlations. It also utilizes zero-copy memory transfers, allowing massive 2D matrices to pass from Python to C++ instantly without slowing down the system.

# The Process
I built this using a microservice-style architecture. I started by writing the data-fetching and statistical analysis modules in Python. Knowing Python is too slow for heavy Monte Carlo loops, I wrote the GBM (Geometric Brownian Motion) math natively in C++. To connect them, I engineered a Pybind11 bridge, allowing the Streamlit UI to hand off the heavy lifting to the compiled C++ binary, entirely bypassing Python's Global Interpreter Lock.

# Learnings
* Learned how to architect cross-language systems and safely manage memory handoffs between Python arrays and C++ vectors.
* Deepened my understanding of quantitative finance mathematics by implementing matrix transformations and random shock simulations entirely from scratch in C++, rather than relying on standard black-box libraries.
* pybind11 , i came to know about it during this project and i immediately shifted from ctypes to it because it's so clean as compared to ctypes

# How to run
* Clone the repository and install the Python dependencies from the requirements.txt file in a virtual environment.
* Run make clean and make in the terminal to compile the C++ engine for your specific machine.
* Run streamlit run app.py to launch the interactive web dashboard.



