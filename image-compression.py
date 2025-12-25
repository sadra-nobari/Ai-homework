import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image

# 1. Load a sample image
img = load_sample_image("china.jpg")
img = np.array(img, dtype=np.float64) / 255 # Normalize

# 2. Reshape to (n_pixels, 3)
w, h, d = img.shape
pixels = np.reshape(img, (w * h, d))

# 3. Apply K-Means to find 16 colors
k = 16
kmeans = KMeans(n_clusters=k, random_state=42).fit(pixels)

# 4. Replace each pixel with its nearest centroid
new_colors = kmeans.cluster_centers_[kmeans.predict(pixels)]
compressed_img = np.reshape(new_colors, (w, h, d))

# 5. Visualize
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].set_title("Original")
ax[1].imshow(compressed_img)
ax[1].set_title(f"Compressed ({k} colors)")
plt.show()