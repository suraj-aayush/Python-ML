import numpy as np

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1 + list2)    # concatenate or joins two list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
a = np.random.randint(0,10,(3,3)) # -> 3x3 ka matrix with random value from 0 to 10
b = np.random.randint(10,20,(3,3))  # -> 3x3 ka matrix with random value from 10 to 20
     

print(a)
print(b)
     
# arithmetic operation 

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# standards

print(np.add(a,b))
print(np.subtract(a,b)) # ->  a[i] - b[i]
print(np.multiply(a,b))
print(np.divide(a,b))   # ->  a[i] / b[i]

# TRANSPOSE of a matrix

trans = np.transpose(a)
print(trans)
print(trans.shape)


# reshaping a array
a = np.random.randint(0,10,(2,3))
print(a)
print(a.shape)
     
# [[4 3 7]
#  [4 6 6]]

# (2, 3)

b = a.reshape(3,2) # RESHAPE
print(b)
print(b.shape)
     
# [[4 3]
#  [7 4]
#  [6 6]]
# (3, 2)