import numpy as np
a=np.arange(11,20).reshape((3,3))
b=np.arange(1,10).reshape((3,3))
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
print("Division of array",np.divide(a,b))
print("---------------")
print("Power of array",np.power(a,b))
print("---------------")
print("Square root of array a",np.sqrt(a))
print("---------------")
print("Square root of array b",np.sqrt(b))
print("---------------")
print("Tranpose of a",np.transpose(a))
print("---------------")
print("Array in horizontal order",np.hstack(a))
print("---------------")
print("Array in vertical order",np.vstack(a))
print("---------------")
print("Arrays are equal or not:",np.array_equal(a,b))
print("---------------")
c=np.arange(1,7).reshape(2,3)
d=c*5
print("Multiplication of array by 5",d)
print("Arrays having zeros:",np.zeros((3,5)))
print("Arrays having ones:",np.ones((3,5)))
print("Maximum:",np.max(a))
print("Mean:",np.mean(a))
print("Median:",np.median(a))
print("Minimum:",np.min(a))
print("Variance:",np.var(a))
print("SD:",np.std(a))
print("Total:",np.sum(a))
print("-------------------")
value,count=np.unique(a,return_counts=True)
print("Unique val are",value)
print("Count is",count)
print("1D array",np.arange(1,10))
a=np.arange(25,40)
print(a)
arr1=np.arange(85,100,1).reshape(3,5)
print(arr1)
print("Random integers",np.random.randint(1,10,(3,3)))