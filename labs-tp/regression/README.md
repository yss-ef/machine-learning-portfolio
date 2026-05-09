# Linear Regression Optimization: Algorithmic Implementation

A comparative study and from-scratch implementation of Linear Regression algorithms in Python. This project explores the mathematical optimization of regression models using both iterative (Gradient Descent) and analytical (Normal Equation) approaches, bypassing high-level machine learning frameworks to focus on core algorithmic logic.

## Technical Overview

The system evaluates two distinct methodologies for solving the linear least squares problem, providing a deep-dive into optimization theory and numerical analysis.

### Core Stack
*   **Engine**: Python 3.10+
*   **Numerical Analysis**: NumPy / Pandas
*   **Data Visualization**: Matplotlib
*   **Data Format**: Excel / OpenPyXL

---

## Optimization Methodologies

### 1. Gradient Descent (Iterative Approach)
A first-order iterative optimization algorithm for finding the local minimum of the Mean Squared Error (MSE) cost function.
*   **Mechanism**: Implements partial derivatives (gradients) for weight ($m$) and bias ($b$) updates.
*   **Mathematical Foundation**:
    $$\theta_{j} := \theta_{j} - \alpha \frac{\partial}{\partial \theta_{j}} J(\theta)$$
*   **Implementation**: Features convergence monitoring via cost history tracking and dynamic hyperparameter tuning (Learning Rate $\alpha$, Epochs).

### 2. Normal Equation (Analytical Approach)
A direct solution using linear algebra to find the global minimum of the cost function without iteration.
*   **Mechanism**: Leverages the Ordinary Least Squares (OLS) closed-form solution.
*   **Mathematical Foundation**:
    $$\theta = (X^{T}X)^{-1}X^{T}y$$
*   **Implementation**: Utilizes NumPy matrix operations to handle the design matrix and target vectors, providing an exact solution for datasets where $X^{T}X$ is invertible.

---

## Technical Features

### Data Processing Pipeline
*   **Ingestion**: Direct extraction of features and labels from raw Excel data.
*   **Feature Mapping**: Automated mapping of independent ($X$) and dependent ($Y$) variables.
*   **Validation**: Error handling for missing data or invalid file paths.

### Analytics & Visualization
*   **Cost Convergence**: Graphical representation of error reduction over time to validate learning rate stability.
*   **Regression Modeling**: Overlay of the calculated model $Y = mX + b$ against the raw scatter data.
*   **Performance Comparison**: Evaluation of iteration count vs. precision for the Gradient Descent engine.

---

## Project Structure

```text
├── gradient-descent.py # Iterative optimization engine
├── linear-regression.py  # Analytical regression model
├── test.xlsx           # Sample dataset for validation
└── README.md           # System documentation
```

---

## Installation & Deployment

### Prerequisites
*   Python 3.10 (or higher)
*   Virtual Environment (Recommended)

### Setup Sequence
1.  **Initialize Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
2.  **Install Dependencies**:
    ```bash
    pip install pandas numpy matplotlib openpyxl
    ```
3.  **Execute Model**:
    ```bash
    python gradient-descent.py
    ```

---

*Authored by Youssef Fellah.*

*Developed for the Engineering Cycle - Mundiapolis University.*
