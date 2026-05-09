# 🔬 Unsupervised Learning Methodologies: Clustering & Segmentation

This repository explores various unsupervised learning algorithms applied to real estate data, focusing on clustering techniques to identify latent patterns and structures. It implements and compares multiple paradigms, including hierarchical, density-based, and centroid-based clustering.

---

## 🛠 Technical Overview

The project focuses on the mathematical and practical implementation of unsupervised learning models:
*   **K-Means Clustering:** Iterative partitioning of data into $k$ distinct clusters based on Euclidean distance.
*   **CAH (Hierarchical Agglomerative Clustering):** Bottom-up clustering using various linkage criteria to build a dendrogram.
*   **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** A density-based approach to identify clusters of arbitrary shapes and detect outliers.

## 💻 Technical Stack

*   **Language:** Python 3.10+
*   **Analysis:** `pandas`, `numpy`
*   **Machine Learning:** `scikit-learn`
*   **Visualization:** `matplotlib`, `seaborn`, `scipy.cluster.hierarchy`

## 📂 Project Structure

```text
├── Tp-CAH/
│   ├── real_estate.csv
│   └── tp-cah.ipynb          # Hierarchical Agglomerative Clustering implementation
├── Tp-DBscan/
│   ├── real_estate.csv
│   └── tp-DBscan.ipynb       # Density-based clustering & outlier detection
├── Tp-K-means/
│   ├── real_estate.csv
│   └── tp-k-means.ipynb      # Centroid-based clustering implementation
└── Tp-comparer/
    ├── real_estate.csv
    └── Projet_Comparatif_final_enonce_corrige.ipynb # Model comparison & evaluation
```

## 🚀 Getting Started

### Prerequisites
*   Python 3.x
*   Jupyter Notebook or JupyterLab

### Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:yss-ef/unsupervised-learning-tp.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn scipy
   ```
3. Launch the notebooks:
   ```bash
   jupyter notebook
   ```

---
*Authored by Youssef Fellah.*
*Developed for the Engineering Cycle - Mundiapolis University.*
