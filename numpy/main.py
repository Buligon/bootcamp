import numpy as np

# ------- The basics -------
""" # a = np.array([1, 2, 3])
a = np.array([1, 2, 3], dtype='int16')
# print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# Get dimension
a.ndim  # "Number dimensions"

# Get shape
a.shape

# Get type
a.dtype

# Get Size
a.itemsize

# Get total size
a.size  # total of elements
a.size * a.itemsize  # 1st way to get the total size
a.nbytes  # another way to do it
 """
# ------- Accessing/Changing specific elements, rows, columns, etc -------
""" a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get a specific element [r, c]
# print(a[1, 5])
# a[1, -2]

# Get a specific row
# print(a[0, :])

# Get a specific column
# print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stesize]
# print(a[0, 1:6:2])

# Changing values
a[1, 5] = 20
# print(a)
# a[:, 2] = 5
a[:, 2] = [1, 2]  # needs to be the same shape
# print(a)
 """
# ------- 3D example -------
""" b = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]])
# print(b)

# Get specific element (work outside in)
b[0, 1, :]
# print(b)

# Replace
b[:, 1, :] = [[9, 9], [7, 7]]
# print(b)
 """
# ------- Initializing different types of arrays -------
"""
# All 0s matrix
c = np.zeros([2, 3])  # all you need to do is specify the shape
# (c.dtype) # default value is float64 btw print
# print(c)

# All 1s matrix
c = np.ones([2, 3], dtype='int32')
# print(c)

# Any other number
c = np.full([2, 2], 99, dtype='float32')
# print(c)

# Any other number (full_like)
c = np.full_like(a, 4)  # it's copying the a matrix shape
# print(c)

# Random decimal numbers
c = np.random.rand(4, 2)  # you still pass the shape
# print(c)
c = np.random.random_sample(a.shape)
# print(c)

# Random integer values
c = np.random.randint(1, 7, size=[4, 5])  # (min, max, shape)
# print(c)

# The identity matrix
c = np.identity(5)
# print(c)

# Filling a matrix with an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
# print(r1)
 """
# ------- Exercise -------
"""
# Mine
c = np.zeros([5, 5])
c[:, 0:5:4] = 1
c[0:5:4, :] = 1
c[2, 2] = 9
# print(c)

# His
output = np.ones((5, 5))
z = np.zeros([3, 3])
z[1, 1] = 9
output[1:4, 1:4] = z
# print(output)
 """
# ------- BE CAREFUL WHEN COPYING ARRAYS -------
a = np.array([1, 2, 3])
b = a  # correct way is: b = a.copy()
b[0] = 100  # this will alter 'a' too
# print(a)
