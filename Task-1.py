l1=["A","B","C"]
l2=["D","E","F"]
l2.reverse()
print("Reverse list",l2)
print("The concatenate list is:",l1+l2)
l4=[i for i in range(21)]
for i in l4:
    if l4[i]==20:
        l4[i]=200
print("Replace",l4)
Marks=[24,12,27,29,30,26,24,20,30,10]
Marks1=[24,12,27,29,30,26,24,20,30,10]
print("OUR LIST",Marks)
Marks[5:5]=[23,27,29,30,12]
print("Inserting marks in the middle of list",Marks)
Marks[15:]=[23,27,29,30,12]
print("Inserting marks in the end of list",Marks)
print("Total students:",len(Marks))
Marks[2]=75
print("Replace the value at index 2",Marks)
print("Last five students:",Marks[-5:])
print("2nd last students",Marks[-2:-1])
for i in range(len(Marks)):
  Marks[i]+=2
Marks2=Marks
print("Grace marks",Marks2)
Marks3=Marks+Marks2
print("Combine list",Marks3)
del Marks3[-5:]
print("deleted",Marks3)
Marks3.sort()
print("Sorted list",Marks3)
print("Maximum marks",max(Marks))
backup=Marks3.copy()
print("Backup",backup)

# l=[i for i in range(5)]
# print(l)
# for i in l:
#     i=i*i
#     print(i)



