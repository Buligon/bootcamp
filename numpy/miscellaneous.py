import numpy as np

# Load data from file
filedata = np.genfromtxt('bootcamp/numpy/data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean masking and Advance indexing
print(filedata > 50)  # return a boolean array
print(filedata[filedata > 50])

# You can index with a list in NumPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])  # [2 3 9]

print(np.any(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=0))

print(((filedata > 50) & (filedata < 100)))
