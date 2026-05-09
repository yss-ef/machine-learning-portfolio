# Unsupervised Learning Methodologies: Clustering & Segmentation

This repository explores various unsupervised learning algorithms applied to real estate data, focusing on clustering techniques to identify latent patterns and structures. It implements and compares multiple paradigms, including hierarchical, density-based, and centroid-based clustering.

---

## Technical Overview

The project focuses on the mathematical and practical implementation of unsupervised learning models:
*   **K-Means Clustering:** Iterative partitioning of data into $k$ distinct clusters based on Euclidean distance.
*   **CAH (Hierarchical Agglomerative Clustering):** Bottom-up clustering using various linkage criteria to build a dendrogram.
*   **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** A density-based approach to identify clusters of arbitrary shapes and detect outliers.

## Technical Stack

*   **Language:** Python 3.10+
*   **Analysis:** `pandas`, `numpy`
*   **Machine Learning:** `scikit-learn`
*   **Visualization:** `matplotlib`, `seaborn`, `scipy.cluster.hierarchy`

## Project Structure

```text
├── hierarchical-clustering/
│   ├── real-estate.csv
│   └── hierarchical-analysis.ipynb          # Hierarchical Agglomerative Clustering implementation
├── dbscan-clustering/
│   ├── real-estate.csv
│   └── dbscan-analysis.ipynb       # Density-based clustering & outlier detection
├── k-means-clustering/
│   ├── real-estate.csv
│   └── k-means-analysis.ipynb      # Centroid-based clustering implementation
└── model-comparison/
    ├── real-estate.csv
    └── clustering-comparison.ipynb # Model comparison & evaluation
```

## Getting Started

### Prerequisites
*   Python 3.x
*   Jupyter Notebook or JupyterLab

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yss-ef/machine-learning-portfolio.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn scipy
   ```
3. Launch the notebooks:
   ```bash
   jupyter notebook
   ```

Authored by Youssef Fellah.  
Developed for the Engineering Cycle - Mundiapolis University.
