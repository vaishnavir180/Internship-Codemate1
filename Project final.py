#!/usr/bin/env python
# coding: utf-8

# ![image-2.png](attachment:image-2.png)
# 
# 

# In[20]:


#Importing the libraries which are mostly used for data analysis and data visualization.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#Importing warning to ignore them.
import warnings
warnings.filterwarnings('ignore')


# In[21]:


#Importing CSV file
data=pd.read_csv('Student Mental health.csv')


# ## Basic and Advanced EDA commands

# In[22]:


#Dipslay top two records
print("The top two records:\n",data.head(2))
#Display bottom two records
print("The bottom two records:\n",data.tail(2))


# In[23]:


#To list down columns
print("The columns of datasets are:\n\n",data.columns,"\n\n")
#tolist also list down the column
print("The columns of datasets are:\n\n",data.columns.values.tolist(),"\n\n")
#iloc() and loc() are used for sclicing purpose
iloc=data.iloc[:,[0,2]]
print("Accesing data:\n\n",iloc,"\n\n")
loc=data.loc[0:2,['Choose your gender','Age']]
print("Accesing data:\n\n",loc)


# In[24]:


#Checking null values and print their total along woth columns
print("Null values with the sum:\n\n",data.isnull().sum())


# In[25]:


#Info() is used to et know about number of enteries.number of columns,data type and memory space it acquired
print(data.info())


# In[26]:


#Describe() is used to get statistical analysis and it only deal with numeric data
print("Statistical analysis:\n\n",data.describe())


# In[27]:


#Returns the count of unqiue values in column
print("The counts of unqiue value:\n\n",data.value_counts())


# In[28]:


#Sample()-returns the random sample of your data
print("Random row:\n",data.sample())


# In[29]:


#For coverting catagorical data into numeric data 
print(data['Do you have Depression?'].replace(['No','Yes'],[0,1],inplace=True))
print(data['Do you have Anxiety?'].replace(['No','Yes'],[0,1],inplace=True))
print(data['Do you have Panic attack?'].replace(['No','Yes'],[0,1],inplace=True))
print(data['Choose your gender'].replace(['Female','Male'],[0,1],inplace=True))


# In[30]:


print(data.info())


# In[31]:


#It retunrs the duplicated value
print("The duplicated values are:\n",data[data.duplicated()])


# ## Visualization of data

# In[32]:


#Box plot:Used to visualize the distribution of a set of data values.
sb.boxplot(x='Do you have Anxiety?',y='Do you have Depression?',data=data)
plt.show()


# ### Obersvations:
# 
# - Students who have depression they also have anxiety.

# ## Univariate Analysis
# - This type of data consists of only one variable.

# In[33]:


#Pie charts-It is used to visualize the distribution of categorical data.
counts0=data['Do you have Depression?'].value_counts()
plt.title('Students have depression',size=24)
print(counts0.plot(kind='pie',autopct=lambda x:f'{x:.0f}%',startangle=90))
plt.show()


# In[1]:


# Create a density plot (KDE) to visualize the distribution of the 'skewed_variable'
data['Do you have Panic attack?'].plot(kind='density', color='b')
plt.xlabel('Do you have Panic attack?')
plt.ylabel('Density')
plt.title('Density Plot of Panic attacks')
plt.show()


# ### Obersvations:
# 
# - Students who have depression they also have anxiety.
# - 35% students have anxiety and depression.

# ## Bivariate analysis:
# 
# - It is a statistical method examining how two different things are related. 

# In[35]:


#Bar plot:It is uesd for comparin the frequency of different categories
counts=data['Did you seek any specialist for a treatment?'].value_counts()
print(counts.plot(kind='bar'))
sb.set_style('whitegrid')
ax = sb.barplot(x=counts.index, y=counts.values, palette='bright')
ax.set_xlabel('Did you seek any specialist for a treatment?')
plt.xticks(rotation=45)
ax.set_ylabel('Number of Students')
plt.title('Specialist treatment',size=24)
plt.show()


# ## Observation
# - It is observe that students who is taking specialist treatment is less compared to students suffering for depression.

# In[36]:


Female = data[data['Choose your gender'] == 0]
Male = data[data['Choose your gender'] == 1]

# Calculate the frequency of depression (1 for Yes, 0 for No) for each gender
c1 = Female['Do you have Depression?'].value_counts()
c2 = Male['Do you have Depression?'].value_counts()

# Create the bar plot
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
c1.plot(kind='bar', ax=ax[0],edgecolor='Black')
c2.plot(kind='bar', ax=ax[1],edgecolor='Black')

# Add labels and title
ax[0].set_title('Frequency of Depression among Females')
ax[0].set_xticklabels(['No', 'Yes'], rotation=0)
ax[0].set_ylabel('Frequency')
ax[1].set_title('Frequency of Depression among Males')
ax[1].set_xticklabels(['No', 'Yes'], rotation=0)
ax[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()


# ## Observation
# - Female count compared to male is more.

# In[37]:


# Assuming you have a pandas DataFrame called 'data' with columns 'Do you have Depression?' and 'Your current year of Study'
# Set the order of the x-axis categories (optional, adjust as needed)
year_order = ['year 1', 'year 2', 'year 3', 'year 4']
plt.figure(figsize=(10, 6))

# Create the count plot with specified order and rotated x-axis labels
sns.countplot(data=data, x='Your current year of Study', hue='Do you have Depression?', palette='Set2', order=year_order)
plt.xlabel('Your current year of Study')
plt.ylabel('Number of Students')
plt.title('Number of Students with Depression by Current Year of Study', size=18)

# Calculate and display percentages for each category
total_students_per_year = data['Your current year of Study'].value_counts()
for i, year in enumerate(year_order):
    count_no_depression = data[(data['Your current year of Study'] == year) & (data['Do you have Depression?'] == 'No')].shape[0]
    count_depression = data[(data['Your current year of Study'] == year) & (data['Do you have Depression?'] == 'Yes')].shape[0]
    total_students = total_students_per_year[year]
plt.legend(title='Depression', labels=['No Depression', 'Depression'])
plt.tight_layout()  # To prevent label cutoff
plt.show()


# ## Multivariate analysis
# It involves evaluating multiple variables (more than two) to identify any possible association among them

# In[38]:


#Heatmap:It uses for visual representation of data with different colors.It is uesd to visualize correlation between variables.
#It lies between -1 to +1
sb.heatmap(data.corr(),annot=True)
plt.title('The heatmap\n',size=24)


# # Conclusion:
# - We observe that student of first year is suffering more it may be because of new environment,adaptibility,etc.
# - We observe that female suffers more than male.
# - We observe that students who have depression they also have anxiety and panic attacks.
# - We observe that students consulting doctor is less the reason ma be that they are not aware about it.
# 
# 
