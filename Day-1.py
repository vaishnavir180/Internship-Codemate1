#Bacics of python
#Division
print(4/5)
#Floor division without decimal
print(4//5)
list=[-5,-4,-3,-2,-1]
print(list[-4:-1])
if -3 in list:
    print("yes")
list[1:3]=[-6]
print(list)

# List comprehension
list=[i for i in range(10) if i%2==0]
print(list)
l1=[12,3]
l2=[i for i in l1]
print(l2)
