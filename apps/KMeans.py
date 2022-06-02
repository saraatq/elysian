import numpy as np

# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster
# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4


def distance(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return np.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


class KMeans:

    def __init__(self, img_arr, k, max_itr=100):
        # objects count
        self.k = k

        # 3d array [i][j][RGB]
        self.img_arr = img_arr
        self.height = len(img_arr[0])       # col
        self.width = len(img_arr)           # row

        # make a list for each k    ~   [[][][]]
        self.objects = [[] for _ in range(self.k)]

        # mean color feature list for each object ~ list of {k} lists
        self.centroids = []

        self.max_itr = max_itr

    def predict(self):
        # initialize centroids

        # random k positions
        # list of random i's    list of random j's
        random_index_i = np.random.choice(self.width, self.k, replace=False)
        random_index_j = np.random.choice(self.height, self.k, replace=False)
        random_index = zip(random_index_i, random_index_j)

        # x[i][j] ~ color ~ feature
        self.centroids = [self.img_arr[i][j] for i, j in random_index]

        # optimization
        for _ in range(self.max_itr):
            # update objects
            self.objects = self.get_objects(self.centroids)

            # update centroids
            old_centroids = self.centroids
            self.centroids = self.get_centroids(self.objects)

            # check if the old centroids = curr centroids
            if self.is_converged(old_centroids, self.centroids):
                break

        # return objects labels
        return self.get_objects_label(self.objects)

    def get_objects(self, centroids):
        objects = [[] for _ in range(self.k)]  # [[] [] []] has positions i, j

        # for each pixel in img arr
        for i in range(self.width):
            for j in range(self.height):
                #  which centroid is near the pixel
                pixel = self.img_arr[i][j]
                centroid_index = self.closest_centroid(pixel, centroids)
                objects[centroid_index].append((i, j))
        return objects

    def closest_centroid(self, pixel, centroids):
        distances = [distance(pixel, point) for point in centroids] # [1 , 3 , 6]
        # return closest index
        return np.argmin(distances)

    def get_centroids(self, objects):
        centroids = []
        for i, object in enumerate(objects):
            # object = [(i, j), (i2, j2), ...]
            # get mean of colors in each object
            object_mean = list(np.mean([self.img_arr[i][j] for i, j in object], axis=0))
            object_mean = [int(m) for m in object_mean]
            centroids.append(object_mean)
        return centroids

    def is_converged(self, old_centroids, centroids):
        distances = [distance(old_centroids[i], centroids[i]) for i in range(self.k)]
        return sum(distances) == 0

    def get_objects_label(self, objects):
        # label every pixel in img_arr
        labels = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for obj_num, object in enumerate(objects):
            for i, j in object:
                labels[i][j] = obj_num
        return labels

    def get_objects_center(self, objects):
        rgb = 3
        center = [[0 for _ in range(rgb)] for _ in range(self.k)]
        for i, object in enumerate(objects):
            center[i] = list(np.median([self.img_arr[i][j] for i, j in object], axis=0))
            center[i] = [int(c) for c in center[i]]
        return center

