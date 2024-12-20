import numpy as np
arr1=list(range(10000))
arr2=list(range(10000,20000))

arr=np.array(arr1)
arr_=np.array(arr2)

# Slower in comparison with numpy arrays
result=0
for x,w in zip(arr1,arr2) :
    result+=x*w
print(result)

# Faster with numpy arrays
m=np.dot(arr,arr_)
print(m)