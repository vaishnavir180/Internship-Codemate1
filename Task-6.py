import pandas as pd
d_data=pd.read_csv('diabetes.csv')
print("Top 5 data of the file\n",d_data.head(5))
print("Bottom 5 data of the file\n",d_data.tail(5))
print("Describe\n",d_data.describe())
print("Attribute infomation\n",d_data.info())
print("List of columns\n",d_data.columns)
print("Null values\n",d_data.isnull)
print("Drop null data",d_data.dropna())
