# E-commerce Customer Segmentation: Unsupervised Machine Learning for Retail Analytics

An end-to-end data science project focused on **Customer Intelligence**. This project uses unsupervised learning algorithms to segment a retail customer base into distinct groups based on annual income, spending behavior, and demographic profiles.

## 🔬 Machine Learning Concepts & Theory

### 1. Unsupervised Learning & Clustering
Unlike supervised learning, clustering does not rely on predefined labels. It identifies hidden patterns in data by grouping similar data points together based on their distance in a multi-dimensional feature space.

### 2. Deep Dive: K-Means Clustering
K-Means is a centroid-based algorithm that partitions $n$ observations into $K$ clusters.
*   **The Centroid Logic**: The algorithm iteratively assigns points to the nearest cluster center and updates the center as the mean of the assigned points.
*   **The Elbow Method**: To determine the optimal $K$, we calculate the **Within-Cluster Sum of Squares (WCSS)**. The "elbow" point in the WCSS graph indicates where adding more clusters no longer provides significant information gain.

### 3. Hierarchical Clustering (CAH)
This project also implements **Agglomerative Hierarchical Clustering**, which builds a hierarchy of clusters.
*   **Dendrograms**: A tree-like diagram used to visualize the sequence of merges. It allows us to determine the optimal number of clusters by observing the longest vertical distance without crossing horizontal lines.
*   **Linkage Criteria**: Uses "Ward's Method" to minimize the variance within each cluster during the merging process.

---

## 🛠 Data Analysis & Modeling Logic

The project follows a rigorous Data Science lifecycle:

1.  **Exploratory Data Analysis (EDA)**: Visualizing distributions of Age, Annual Income, and Spending Score using Seaborn and Matplotlib.
2.  **Feature Engineering**: Selecting relevant features for segmentation (Income vs. Spending Score) and handling data scaling.
3.  **Model Implementation**:
    *   **K-Means**: Identifying 5 distinct segments (The VIPs, The At-Risk, The Careful, The Average, and The Spenders).
    *   **Hierarchical Clustering**: Validating cluster stability using dendrogram analysis.
4.  **Explicability**: Interpreting the clusters to provide actionable business recommendations.

---

## 📂 Project Structure

*   `ML_Sujet2.ipynb`: Complete Google Colab notebook containing data cleaning, visualization, and modeling.
*   `Segmentation_Clients_Ecommerce.pptx`: Executive summary and business results presentation.
*   `*.png`: Exported visualizations (Elbow Method, Dendrograms, K-Means Clusters).

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Jupyter Notebook or Google Colab
*   Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yss-ef/ecommerce-customer-segmentation.git
   ```
2. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. **Run the Analysis**:
   Open `ML_Sujet2.ipynb` in your preferred notebook environment.

---

*Authored by Youssef Fellah.*

*Developed as part of the Academique Portfolio.*
