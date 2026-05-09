# Machine Learning Labs & Mini-Projects Collection

A consolidated repository containing various Machine Learning pedagogical exercises (Labs/TPs) and applied mini-projects (Subjects).

## Repository Structure

```text
ml-labs-collection/
├── data/                    # Centralized datasets (deduplicated)
│   └── raw/                 # Original CSV/XLSX files
├── mini-projects/           # Applied subjects and mini-projects
│   ├── subject-01-ecommerce/ # E-commerce Customer Segmentation (Clustering)
│   └── subject-02-telecom/   # Telecom Churn Analysis (Classification)
├── labs-tp/                 # Pedagogical exercises (TPs)
│   ├── basic-exercises/     # Fundamentals of ML with Scikit-learn
│   ├── clustering/          # K-Means, DBSCAN, and Hierarchical Clustering
│   ├── course-labs/         # Miscellaneous course-related mini-projects
│   └── regression/          # Linear and Multiple Regression implementations
└── requirements.txt         # Unified dependencies
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Notebooks**:
   Navigate to any project directory and launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Key Projects

### Mini-Projects (Subjects)
- **Subject 01: E-commerce Segmentation**: Unsupervised learning project to identify customer segments.
- **Subject 02: Telecom Churn**: Classification project to predict customer attrition.

### Labs (TPs)
- **Clustering**: Comparative analysis of different clustering algorithms on real estate data.
- **Regression**: From-scratch implementation of Gradient Descent and Multiple Linear Regression.

## History
This repository was consolidated from 6 individual repositories while preserving the full commit history of each project.
