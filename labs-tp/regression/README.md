# Linear regression optimization: algorithmic implementation

This project provides a comparative study and implementation of linear
regression algorithms in Python. It explores the mathematical optimization of
regression models using iterative gradient descent and analytical normal
equation approaches.

## Technical overview

The system evaluates two methodologies for solving the linear least squares
problem, focusing on optimization theory and numerical analysis.

### Core stack

- Engine: Python 3.10 or later
- Numerical Analysis: NumPy and Pandas
- Data Visualization: Matplotlib
- Data Format: Excel (OpenPyXL)

## Optimization methodologies

### 1. Gradient descent

This first-order iterative optimization algorithm finds the local minimum of
the mean squared error (MSE) cost function.
- Mechanism: Implements partial derivatives for weight and bias updates.
- Implementation: Monitors convergence through cost history tracking and
  dynamic hyperparameter tuning.

### 2. Normal equation

This analytical approach uses linear algebra to find the global minimum of the
cost function without iteration.
- Mechanism: Uses the ordinary least squares (OLS) closed-form solution.
- Implementation: Utilizes NumPy matrix operations for exact solutions on
  compatible datasets.

## Technical features

### Data processing pipeline

- Ingestion: Extracts features and labels from raw Excel data.
- Feature mapping: Automatically maps independent and dependent variables.
- Validation: Implements error handling for missing data or invalid paths.

### Analytics and visualization

- Cost convergence: Represents error reduction over time to validate learning
  rate stability.
- Regression modeling: Overlays the calculated model against raw scatter data.
- Performance comparison: Evaluates iteration count versus precision for
  gradient descent.

## Project structure

- `gradient-descent.py`: The iterative optimization engine.
- `linear-regression.py`: The analytical regression model.
- `test.xlsx`: Sample dataset for validation.

## Installation and deployment

1. Initialize the environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib openpyxl
   ```
3. Execute the model:
   ```bash
   python gradient-descent.py
   ```

Authored by Youssef Fellah.
Developed for the Engineering Cycle at Mundiapolis University.
