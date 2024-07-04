import numpy as np
#Shallow copy a=b and deep copy( )
a=np.array([1,2,3,4,5])
print(id(a))
b=a
print(id(b))
print(b)
c=np.copy(a)
print(id(c))
a[1]=7
print(a,c)
print("-------------------------------")

#Arrange()
print("Even numbers array",np.arange(0,11,2))
print("-------------------------------")

#Linespace It is used for genrating numbers we want to display
print(np.linspace(1,11,10))
print(np.linspace(41,67,4))
print("-------------------------------")

#Random()
import random
print(np.random.random())
print("Random numbers with dimensions",np.random.randn(2,3))
print("Single Random numbers",np.random.randn())
print("Random integers",np.random.randint(1,5))
print("Random integers",np.random.randint(1,5,5))
print("Random integers \n",np.random.randint(1,5,(2,2)))
np.random.seed(10)
print("Genrating same value",np.random.randint(1,11,2))
print("-------------------------------")

#ravel Retrun 1D array
x=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(x)
print(np.ravel(x))
print("-------------------------------")

#Creating arrays of 1's and 0's
print(np.zeros((2)))
print(np.ones((2,2)))
d=np.full((3,3),2)
print(d)
#Identity matrix
print(np.eye(3))
print("-------------------------------")

#Unique functions
a1=np.array([1,2,3,4,3,2,5])
print(np.unique(a1))
value,count=np.unique(a1,return_counts=True)
print("Unique val are",value)
print("Count is",count)

#Checking array is same or not
a2=np.arange(1,16).reshape(3,5)
print(a2)
a3=np.arange(1,16).reshape(3,5)
print(a3)
print("Arrays are equal or not: ",np.array_equal(a2,a3))
a3[0,2]=4
print("Arrays are equal or not: ",np.array_equal(a2,a3))

