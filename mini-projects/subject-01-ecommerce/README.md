# E-commerce customer segmentation: retail analytics

This project uses unsupervised learning algorithms to segment a retail
customer base into distinct groups. The segmentation is based on annual
income, spending behavior, and demographic profiles.

## Machine learning concepts

### 1. Unsupervised learning and clustering

Clustering identifies hidden patterns in data by grouping similar data points
together. It does not rely on predefined labels.

### 2. K-means clustering

K-means is a centroid-based algorithm that partitions observations into
distinct clusters.
- Centroid logic: The algorithm iteratively assigns points to the nearest
  cluster center and updates the center based on the mean of those points.
- Elbow method: The optimal number of clusters is determined by calculating
  the within-cluster sum of squares (WCSS).

### 3. Hierarchical clustering (CAH)

Agglomerative hierarchical clustering builds a hierarchy of clusters.
- Dendrograms: These tree-like diagrams visualize the sequence of merges and
  help determine the optimal number of clusters.
- Linkage criteria: The project uses Ward's method to minimize variance within
  each cluster during merging.

## Data analysis and modeling logic

The project follows a standard data science lifecycle:

1. Exploratory data analysis (EDA): Visualizes distributions of age, income,
   and spending scores.
2. Feature engineering: Selects relevant features for segmentation and handles
   data scaling.
3. Model implementation: Uses K-means and hierarchical clustering to identify
   and validate distinct customer segments.
4. Explicability: Interprets clusters to provide actionable business
   recommendations.

## Project structure

- `customer-segmentation.ipynb`: Contains data cleaning, visualization, and
  modeling analysis.
- `customer-segmentation-report.pptx`: Provides an executive summary and
  business results.
- `*.png`: Includes exported visualizations like dendrograms and cluster
  plots.

## Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/yss-ef/machine-learning-portfolio.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Run the analysis in a notebook environment.

Authored by Youssef Fellah.
Developed for the Engineering Cycle at Mundiapolis University.
