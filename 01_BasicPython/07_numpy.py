import numpy as np
from time import process_time
a = np.array([1,2,3,4])
# print(a)
# print(a[2])

print(a.shape) # gives the row and colm

b = np.array( [(1,2,3,4), (5,6,7,8)] )
# print(b)
# print(b[1])
# print(b[0][2])
# print(type(b))

print(b.shape) #gives the row and colm

#/////////////////////////////////////////////////////
# checking the time difference

# # //// normal list
# a=[i for i in range(10000)]
# start = process_time()

# a = [i+5 for i in range(10000)]
# end = process_time()

# print(end-start)

# # //// NP Array
# b = np.array(i for i in range(10000))
# start_time = process_time()

# np.array += 5
# end_time = process_time()

# print(end_time - start_time)
#//////////////////////////////////////////////////////


