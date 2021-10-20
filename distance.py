import numpy as np

def cosine_distance(x, y):
    print("Calculating distance...")
    x_transpose = np.transpose(x)
    numerator = x_transpose * y
    denominator = np.linalg.norm(x) * np.linalg.norm(y)
    return numerator / denominator

print("Hello cosine distance function")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(cosine_distance(x, y))
