#Numpy
#Statistical array
import numpy as np
a=np.array([[[1,2,6,5,5],[1,2,6,5,5]],[[1,2,6,5,5],[1,2,6,5,5]]])
a1=np.array([1,2,6,5,5])
#Sorting
print("Ascending order",np.sort(a))
print("Descending order:",np.sort(a)[::-1])
print("3D array: ",a[0,1,1])
print("Maximum:",np.max(a))
print("Mean:",np.mean(a))
print("Median:",np.median(a))
print("Minimum:",np.min(a))
print("Variance:",np.var(a))
print("SD:",np.std(a))
print("Total:",np.sum(a))
import numpy as np
a=np.array([[1,2],[2,4]])
print(a)
b=np.array([[[1,2],[2,5]],[[1,2],[2,4]],[[1,2],[2,4]]])
print(b)
print(b.shape)
b1=np.array([[1,2,3],[4,5,6]])
b2=np.array([[7,8,9],[10,11,12]])
print("Joining two arrays",np.concatenate((b1,b2)))
c=b*5
print('---------')
print(c)
c1=b/5
print('---------')
print(c1)
c2=b+5
print('---------')
print(c2)
c3=b**2
print('---------')
print(c3)
print(a.ndim)

#ARRANGE OR RANGE IN NUMPY
a=np.arange(1,5).reshape((2,2))
b=np.arange(1,5).reshape((2,2))
# Arithmatic Operation
print("---------------")
print("Addition of array",np.add(a,b))
print("---------------")
print("Subtraction of array",np.subtract(a,b))
print("---------------")
print("Modulus of array",np.mod(a,b))
print("---------------")
print("Multiplication of array",np.multiply(a,b))
print("---------------")
print("power of array",np.power(a,b))
print("---------------")
#Transpose,horizontal and vertical 
print("Array a",a)
print("---------------")
print("Transpose of array",np.transpose(a))
print("---------------")
print(np.hstack((a,b)))
print("---------------")
print(np.vstack((a,b)))