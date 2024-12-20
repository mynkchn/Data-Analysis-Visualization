# Importing NumPy library
import numpy as np 

# Creating a Zero matrix 
m = np.zeros((2,3))
print("Zero Matrix:")
print(m)

# Identity matrix
n = np.eye(3)
print("\nIdentity Matrix:")
print(n)

# Containing only 1 matrix
s = np.ones([2,3,4])
print("\nMatrix of Ones:")
print(s)

# Full matrix with same element
k = np.full([2,3],42)
print("\nFull Matrix with Same Element:")
print(k)

# Random vector
l = np.random.rand(5)
print("\nRandom Vector:")
print(l)

# Random matrix
p = np.random.randn(2,3)
print("\nRandom Matrix:")
print(p)

# Important - a range function
i = np.arange(3,90,10)
print("\nRange Function:")
print(i)

# Linspace function
d = np.linspace(3,27,12)
print("\nLinspace Function:")
print(d)
