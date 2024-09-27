import numpy as np
from sklearn.cluster import KMeans

N = 40
SIGMA = 0.05

def print_point(x: float, y: float, color: str):
    print(f"\\node[circle,fill=black,inner sep=1pt, color={color}] at ({x},{y}) {"{}"};")


if __name__ == '__main__':
    np.random.seed(0)
    D1 = np.random.random(N)
    D2 = np.random.random(N)

    R1 = np.random.normal(1, SIGMA, N)
    R2 = np.random.normal(2, SIGMA, N)

    A = np.array([R1 * np.cos(2 * np.pi * D1), R1 * np.sin(2 * np.pi * D1)])
    B = np.array([R2 * np.cos(2 * np.pi * D2), R2 * np.sin(2 * np.pi * D2)])

    X = np.concatenate((A.T, B.T), axis=0)

    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

    # points in cluster 0
    for x, y in X[kmeans.labels_ == 0]:
        print_point(x, y, 'mygreen')

    print('% -----------------')

    # points in cluster 1
    for x, y in X[kmeans.labels_ == 1]:
        print_point(x, y, 'myblue')





