import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 1. Generate synthetic data
n_samples = 300
centers = 4
X, y_true = make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.70, random_state=42)

# 2. Implement K-Means Algorithm from scratch
def k_means(X, k, max_iters=100):
    # Randomly initialize centroids by picking k data points
    n_samples, n_features = X.shape
    indices = np.random.choice(n_samples, k, replace=False)
    centroids = X[indices]
    
    for i in range(max_iters):
        # Step 1: Assign each point to the nearest centroid
        # distances shape: (n_samples, k)
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Step 2: Compute new centroids as the mean of the assigned points
        new_centroids = np.array([X[labels == j].mean(axis=0) if len(X[labels == j]) > 0 
                                  else centroids[j] for j in range(k)])
        
        # Check for convergence (if centroids don't change)
        if np.allclose(centroids, new_centroids):
            print(f"Converged at iteration {i}")
            break
        centroids = new_centroids
        
    return centroids, labels

# Run the algorithm
k = 4
centroids, labels = k_means(X, k)

# 3. Visualize the result
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', alpha=0.7, edgecolors='k')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=250, marker='X', label='Centroids')
plt.title(f'K-means Clustering Results (k={k})')
plt.legend()
plt.savefig('kmeans_clustering.png')