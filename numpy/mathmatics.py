import numpy as np

# ------- Mathematics -------
""" a = np.array([1, 2, 3, 4])
a += 2
# print(a)  # [3 4 5 6]
a -= 2
# print(a)  # [1 2 3 4]
a *= 2
# print(a)  # [2 4 6 8]
a = a / 2
# print(a)  # [1. 2. 3. 4.]

b = np.array([1, 0, 1, 0])
c = a + b
print(c)

a = a ** 2
print(a)

# take the sin and cos
a = np.sin(a)
print(a)
a = np.cos(a)
print(a)
 """
# For more (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

# ------- Linear Algebra -------
a = np.ones([2, 3])
print(a)

b = np.full([3, 2], 2)
print(b)

c = np.matmul(a, b)
print(c)

# Find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# Reference (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...

# ------- Statistics -------

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)

# print(np.min(stats))
print(np.min(stats, axis=0))
print(np.max(stats))

print(np.sum(stats, axis=0))
