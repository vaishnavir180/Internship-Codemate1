#Collection datatype
x=("apple","Kiwi","Orange","Melon")
y=list(x)
y[1]="Cherry"
x=tuple(y)
print(x)
print(type(x))
x1=("apple","Kiwi","Orange","Melon")
(a,b,*c)=x1
print(a)
print(b)
print(c)
# For loop
for i in x1:
    print(i)
#Mutiple
x2=x1*2
print(x2)
print(x2.count("apple"))
print(x2.index("apple"))
x3=list(x2)
x3.sort()
print(tuple(x3))

#Set
set1={"a","b","c","d"}
set2={"a","e","o"}
print("n" in set1)
#Doesn't throw error in case of discard
set1.discard("e")
print(set1)
set1.remove("e")
print(set1)

#delete and clear
set2.clear()
print(set2)
del set1
print(set1)

#UNION  
set3=set1.union(set2)
print(set3)
#INTERSECTION
set4=set1.intersection(set2)
print(set4)
print(set2-set1)
print(set1.difference(set2))

#Dictonary
dict={"Name":"ADX","Age":"19","Class":"X"}
print(dict)
print(dict["Age"])
x=dict.items()
print(x)
x1=dict.keys()
print(x1)
x2=dict.values()
print(x2)
dict["Age"]=20
print(dict)
dict.update({"Age":21})
print(dict)
dict.popitem()
print(dict)
mydict=dict.copy()
print(mydict)
l1=["A","B","C"]
l2=[10,20,30]
d1=dict(zip(l1,l2))
print(d1)

#Decision making
a=45
b=3
if a>b:
    pass
print("Hii")
i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#FUNCTIONS
def var(a):
    b=a+10
    return b
print(var(2))
x=lambda a: a+23
print(x(5))
x=lambda a,b: a*b
print(x(5,8))