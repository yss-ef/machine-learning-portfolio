# Unsupervised learning methodologies: clustering and segmentation

This repository explores unsupervised learning algorithms applied to real
estate data. It focuses on clustering techniques to identify latent patterns,
implementing and comparing hierarchical, density-based, and centroid-based
paradigms.

## Technical overview

The project focuses on the mathematical and practical implementation of
unsupervised models:
- K-means clustering: Partitions data into distinct clusters based on Euclidean
  distance.
- Hierarchical agglomerative clustering (CAH): Uses linkage criteria to build
  dendrograms.
- DBSCAN: Identifies clusters of arbitrary shapes and detects outliers using a
  density-based approach.

## Technical stack

- Language: Python 3.10 or later
- Analysis: Pandas, NumPy
- Machine Learning: Scikit-learn
- Visualization: Matplotlib, Seaborn, Scipy

## Project structure

- `hierarchical-clustering/`: Implementation of hierarchical agglomerative
  clustering.
- `dbscan-clustering/`: Implementation of density-based clustering and outlier
  detection.
- `k-means-clustering/`: Implementation of centroid-based clustering.
- `model-comparison/`: Comparison and evaluation of clustering models.

## Getting started

### Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yss-ef/machine-learning-portfolio.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn scipy
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

Authored by Youssef Fellah.
Developed for the Engineering Cycle at Mundiapolis University.
