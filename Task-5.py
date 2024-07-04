import pandas as pd
mydata={
'Temperature': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
'Pressure': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
}
df=pd.DataFrame(mydata)
print(df)
df.to_csv('temp.csv')
pd.read_csv('temp.csv')
df.head(3)
df.tail(3)
df.describe()
df.shape
df.columns
df.info()
mark1 = pd.Series([80, 85, 90, 75, 95])
mark2 = pd.Series([70, 88, 92, 79, 85])
#addition
a=mark1+mark2
print("addition:\n",a)
#substraction
b=mark1-mark2
print("substraction:\n",b)
#multiplication
c=mark1*mark2
print("multiplication:\n",c)
#division
d=mark1/mark2
print("division:\n",d)
student_info={
'Name' : ['Jay','Rohan','Prathamesh','Ansh','Aditya',
'Pallavi','Ruchika','Saloni','Sahatsh','Tanishq'],
'Roll No.' : [15,34,12,32,43,13,67,45,9,78],
'Marks' : [87,78,79,89,87,60,88,68,79,80]
}
df=pd.DataFrame(student_info)
print(df)
df.to_csv('student.csv')
pd.read_csv('student.csv')
df.head()
df.tail()
print("Number of records:", df.shape[0])
print("Number of attributes:", df.shape[1])
# Minimum
minimum = df['Marks'].min()
print('Minimum:',minimum)
#Maximum
maximum = df['Marks'].max()
print('Maximum:',maximum)
#count
count = df['Marks'].shape[0]
print('Count:',count)
#mean
mean=df['Marks'].mean()
print('Mean:',mean)
#median
median=df['Marks'].median()
print('Median:',median)