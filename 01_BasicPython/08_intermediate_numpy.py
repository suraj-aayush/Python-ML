import numpy as np

print("Creating float type np array")
c = np.array([(1,2,34,5), (6,7,8,9)], dtype=float)
print(c)
print(c.shape)
print(type(c))

# creating an array of zeroes
print("NP array of zeros")
d = np.zeros((2,3))
print(d)

# creating an array of ones
print("NP array of ones")
e = np.ones((3,4))
print(e)

# creating an array of any values
print("any value")
f = np.full( (3,4), 9 ) #creates and array of 3 x 4 , and all values = 9
print(f)

# creating identity matrix... diagonal = 1 and all 0

g = np.eye((2)) # should be a square matrix of 2x2
print(g) 

# create a numpy array with random values
b = np.random.random((3,4))
print(b)

# random integer values array within a specific range
c = np.random.randint(10,100,(3,5))  #  3x5 ka matrix and value betn 10 - 100
print(c)

# number of dimensions
print(c.ndim)   # o/p ->  2 .... 2 dimensional array

# number of elements in an array
print(c.size)  # o/p ->   25
      
