#SINGLE TUPLE
print("Tuple")
t1=("50",)
print(t1)
t2=(1,2,3,4)
(a,b,c,d)=t2
print(a)
print(b)
print(c)
x=("Mango","Kiwi","Orange","Melon")
y=list(x)
y[2]="Apple"
x=tuple(y)
print(x)
x1=list(x)
x1.sort()
x=tuple(x1)
print(x)
x2=(1,2,35,50,50)
print(x1.count(50))
print(x2[-2:])
fruit=("kiwi","Melon")
stu=("Ayushi","Khushie")
print(fruit+stu)
print("-----------------")

#SET
print("SET")
a={1,2,3,4,5}
b={11,2,33,4,55}
#Returning identical value
print(a.intersection(b))
#Displaying both set with no duplicate value
print(a.union(b))
#Display element present in A
print(a-b)
#Copy one set to another
c=a.copy()
print(c)
print("-----------------")
#Dictionary
print("DICTIONARY")
d1={'Name':"XYZ","Rollno":16,"Branch":"CSE","Contact":1234}
#Deleting branch
d1.pop("Branch")
print(d1)
#Updating the name
d1 ["Name"]="RAM"
print(d1)
#Fetching keys,values and both
print(d1.keys())
print(d1.values())
print(d1.items())
#Copy d1 to d2
d2=d1.copy()
print(d2)
print("-----------------")
#Decision making
#Factorial of a number
print("Decision making and loops")
def fact(n):
    return 1 if(n==0 or n==0) else n*fact(n-1)
num=5
f=fact(num)
print("Factorial of",num,"is",f)

#Natural number
Num=[i for i in range(11)]
print(Num)

#   Addition of three numbers
def add(a,b,c):
    add=a+b+c
    return add
a1=6
b1=5
c1=4
sum=add(a1,b1,c1)
print("Addition of number is:",sum)





