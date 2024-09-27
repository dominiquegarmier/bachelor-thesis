import numpy as np

N = 40
SIGMA = 0.05

def print_point(x,y):
    print(f"\\node[circle,fill=black,inner sep=1pt] at ({x},{y}) {"{}"};")


if __name__ == '__main__':
    D1 = np.random.random(N)
    D2 = np.random.random(N)

    R1 = np.random.normal(1, SIGMA, N)
    R2 = np.random.normal(2, SIGMA, N)

    A = np.array([R1 * np.cos(2 * np.pi * D1), R1 * np.sin(2 * np.pi * D1)]).T.tolist()
    B = np.array([R2 * np.cos(2 * np.pi * D2), R2 * np.sin(2 * np.pi * D2)]).T.tolist()

    for a, b in A:
        print_point(a, b)

    input()

    for a, b in B:
        print_point(a, b)

