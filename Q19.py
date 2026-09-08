#using numpy create a 2D array of size 4x5 and print the array
import numpy as np

array = np.arange(20).reshape(4, 5)
print(array)

#print the array in a 2D format
print(array.shape)
print(array.size)
print(array.ndim)
print(array.dtype)
print(array.itemsize)
print(array.nbytes)
print(array.strides)