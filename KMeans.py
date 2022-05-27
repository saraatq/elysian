import numpy as np
import matplotlib.pyplot as plt


# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster
# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4


def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KMeans:

    def __init__(self, k, max_itr=100):
        self.k = k
        self.max_itr = max_itr

        # make a list for each k
        self.clusters = [[] for _ in range(self.k)]

        # mean feature list for each cluster
        self.centroids = []

    def predict(self, x):
        self.x = x
        self.n_samples = self.n_features = (x.shape[0] - 1, x.shape[1])

        # initialize centroids , len = k
        random_sample_index = np.random.choice(self.n_samples, self.k, replace=True)
        self.centroids = [self.x[i] for i in random_sample_index]

        # optimization
        for _ in range(self.max_itr):
            # update clusters
            self.clusters = self.create_clusters(self.centroids)

            # update centroids
            old_centroids = self.centroids
            self.centroids = self.get_centroids(self.clusters)

            # check if the old centroids = curr centroids
            if self.is_converged(old_centroids, self.centroids):
                break

        # return cluster labels
        return self.get_cluster_label(self.clusters)

    def create_clusters(self, centroids):
        clusters = [[] for _ in range(self.k)]
        for i, sample in enumerate(self.x):
            centroid_index = self.closest_centroid(sample, centroids)
            clusters[centroid_index].append(i)
        return clusters

    def closest_centroid(self, sample, centroids):
        distances = [distance(sample, point) for point in centroids]
        # return closest index
        return np.argmin(distances)

    def get_centroids(self, clusters):
        centroids = []
        for i, cluster in enumerate(clusters):
            cluster_mean = np.mean([self.x[c] for c in cluster], axis=0)
            centroids.append(cluster_mean)
        return centroids

    def is_converged(self, old_centroids, centroids):
        distances = [distance(old_centroids[i], centroids[i]) for i in range(self.k)]
        return sum(distances) == 0

    def get_cluster_label(self, clusters):
        labels = np.empty(self.n_samples)
        for i, cluster in enumerate(clusters):
            for sample_index in cluster:
                labels[sample_index] = i
        return labels

    def get_cluster_center(self, clusters):
        center = np.empty(self.n_samples)
        for i, cluster in enumerate(clusters):
            center[i] = np.median(cluster, axis=1)
        return center

    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.x[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color="black", linewidth=2)

        plt.show()
