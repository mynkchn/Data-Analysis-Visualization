import numpy as np
m=np.array([1,2,3,4,5])
for n in m :
    print(n)
n=np.array([1,2,3,4,5])
print(type(n))
print(n.dtype)
print(m)
kanto=np.array([70,34,23])
weights=np.array([0.2,0.3,0.4])
# Dot product
print(np.dot(kanto,weights))
print((kanto*weights).sum())