#PANDAS
import pandas as pd
import numpy as np
my_list=[10,20,30]
lables=['X','Y','Z']
#Creating series with desired labels
var=pd.Series(data=my_list,index=lables)
print(var)
#Accessing list using index
print(var[1])
#Type check
print(type(var))
#Arithmatic operation
a=pd.Series([1,2,3])
b=pd.Series([3,5,6])
print("Addition of series\n",a+b)
print("Division of series\n",b/a)
print("-------------------------------")
#print(np.random.randn(10,5))
#Creating datasets
sample=pd.DataFrame(data=np.random.randn(10,5),index='A B C D E F G H I J'.split(),columns='Score1 Score2 Score3 Score4 Score5'.split())
print(type(var))
#Accessing data from columns
print(sample['Score1'])
print(sample)
print(sample[['Score1','Score3']])
#Arithmatics operations between colums
Score6=sample['Score2']+sample['Score1']
print(Score6)
print(sample)
print("-------------------------------")
#Drop row axis=0
new=sample.drop('A',axis=0,inplace=True)
print(new)
print(sample)
print("-------------------------------")
#Loc() and iloc() both fuction are used for idexin and slicing
#Using labels
var1=sample.loc['F']
print(var1)
#Usin index
var2=sample.iloc[3]
print(var2)
#Using Slicing
var3=sample.iloc[0:3]
print(var3)
var4=sample.iloc[0:3,0:3] #row(start:end,col(start,end))
print(var4)
#Getting specified values with column and row
var5=sample.loc['F','Score4']
print(var5)
print("-------------------------------")
print(sample[sample>0.5])
print("-------------------------------")
print(sample[sample['Score1']>0.5]['Score1'])
print(sample[sample['Score3']>0.5][['Score3','Score5']])
var5=sample[(sample['Score1']>0.5) & (sample['Score5']>0.2)]
print(var5)
print("-------------------------------")


