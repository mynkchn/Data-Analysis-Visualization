import numpy as np

arr=np.array([1,2,3,4,5])
arr_1=np.array([1,2,3,4,5])

# scalar operations on arrays
print(arr+1)
print(arr/1)
print(arr//2)
print(arr*2)
print(arr%2)

#   Arthimetic operations on arrays also know as array broadcasting
print(arr+arr_1) #np.add(arr,arr_1)
print(arr*arr_1) #np.multiply(arr,arr_1)
print(arr-arr_1) #np.subtract(arr,arr_1)
print(arr/arr_1)
print(arr//arr_1)
print(arr%arr_1)

print(arr.sum())
print(arr.max())