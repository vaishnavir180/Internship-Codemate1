import seaborn as sns
import pandas as pd 

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('diabetes.csv')
df.head()
df.corr()  
sns.heatmap(df.corr(),annot = True,cmap = 'bwr')
sns.jointplot(x='Age',y='Pregnancies',data = df,kind = 'hex')
sns.pairplot(df[['Glucose','BloodPressure','SkinThickness','Insulin','Outcome']],hue='Outcome')
sns.pairplot(df[['Glucose','BloodPressure','SkinThickness','Insulin']],hue='Insulin')
sns.distplot(df['Age'])
sns.countplot(x=df['Outcome'])
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))
sns.barplot(x ='Age',y = 'Outcome',data =df)
sns.boxplot(x='Age',data = df)
sns.violinplot(x=df['Age'],pallete='rainbow')