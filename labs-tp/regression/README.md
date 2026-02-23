# 📈 Simple Linear Regression Implementations

> **Academic Project - Multidimensional Data Analysis**
> This repository presents a from-scratch Python implementation of Simple Linear Regression (). It explores and contrasts two fundamental approaches for calculating the model's coefficients using datasets provided in Excel format.

## 📑 Table of Contents

* [Methodology Comparison](https://www.google.com/search?q=%23-methodology-comparison)
* [Method 1: Gradient Descent](https://www.google.com/search?q=%23-method-1-gradient-descent-iterative-approach)
* [Method 2: Normal Equation](https://www.google.com/search?q=%23-method-2-normal-equation-analytical-approach)
* [Installation & Setup](https://www.google.com/search?q=%23%EF%B8%8F-installation--setup)
* [Usage Guide](https://www.google.com/search?q=%23-usage-guide)

## ⚖️ Methodology Comparison

| Feature | Gradient Descent | Normal Equation |
| --- | --- | --- |
| **Approach** | Iterative Optimization | Analytical / Matrix Algebra |
| **Hyperparameters** | Requires tuning (Learning Rate, Epochs) | None |
| **Computational Complexity** | Efficient for massive datasets () | High for very large feature sets () |
| **Dependencies** | `pandas`, `matplotlib` | `pandas`, `numpy` |

## 📉 Method 1: Gradient Descent (Iterative Approach)

This approach utilizes **Gradient Descent**, a first-order iterative optimization algorithm used to minimize the Mean Squared Error (MSE) cost function and find the optimal coefficients.

### ✨ Features

* **Data Ingestion:** Reads datasets directly from `.xlsx` files.
* **Iterative Calculation:** Progressively updates the slope (`a`) and intercept (`b`).
* **Data Visualization:** Uses Matplotlib to plot the regression line against the scatter data and visualizes the cost function's convergence curve.
* **Hyperparameter Tuning:** Adjustable learning rate and iteration count.

### 🧠 Concept

Gradient descent aims to locate the minimum of the error function by moving in the direction of the steepest descent. Similar to a hiker finding the lowest point of a valley in dense fog by taking steps down the steepest slope, the algorithm updates the coefficients at each iteration until it converges to the optimal values.

## 🧮 Method 2: Normal Equation (Analytical Approach)

This second approach leverages the **Ordinary Least Squares (OLS)** method via the Normal Equation, utilizing linear algebra to find a direct, analytical solution.

### ✨ Features

* **Data Ingestion:** Reads datasets directly from `.xlsx` files.
* **Automatic Calculation:** Instantly computes the exact slope (`a`) and intercept (`b`).
* **Pure Implementation:** Relies strictly on NumPy matrix operations without high-level Machine Learning libraries (like Scikit-learn).

### 🧠 Concept

The calculation provides a closed-form solution to the least squares problem. The Normal Equation is defined as:

Where:

*  is the vector containing the coefficients `b` (intercept) and `a` (slope).
*  is the vector of the dependent variable values.
*  is the design matrix, consisting of a column of 1s (for the intercept) and a column containing the independent variable values.

## 🛠️ Installation & Setup

To run this project on **Fedora 43**, it is highly recommended to use a Python virtual environment to avoid conflicts with system packages.

**1. Create and activate a virtual environment:**

```bash
python3 -m venv regression_env
source regression_env/bin/activate

```

**2. Install required dependencies:**

```bash
pip install pandas numpy matplotlib openpyxl

```

## 🚀 Usage Guide

**1. Prepare your dataset:**

* Create an Excel file (e.g., `donnees.xlsx`).
* **Column A:** Dependent variable data ().
* **Column B:** Independent variable data ().
* *Note: The file must not contain headers.*

**2. Configure the script:**

* Open the Python script (e.g., `ModRegression-1.py`).
* Update the file path variable to match your dataset:
```python
chemin_fichier = 'donnees.xlsx'

```



**3. Execute the script:**

```bash
python ModRegression-1.py

```

**4. Review the Output:**
The terminal will display the calculated slope (`a`), intercept (`b`), and the final equation of your mathematical model. For the Gradient Descent method, graphical plots will also be generated.

---

*Authored by Youssef Fellah.*
