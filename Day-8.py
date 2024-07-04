#Seaborn [Heatmap(mutlibreate),joinplot,pairplot,distplot, count plot,barpot,box plot,violin plot]Advanced version of matplotlib
import seaborn as sb
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv('diabetes.csv')
#heatmap
data.corr()
sb.heatmap(data.corr(),annot=True,cmap='bwr')
