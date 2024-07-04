import pandas as pd
import numpy as np
s=pd.DataFrame(data=np.random.randn(7,7),index='X1 X2 X3 X4 X5 X6 X7'.split(),columns='A1 A2 A3 A4 A5 A6 A7'.split())
print("My dataset\n",s)
print("Value >.5\n",s[s>0.5])
print(s[s['A7']>0.5]['A7'])
print(s.iloc[4:7])
print(s.iloc[0:3,0:3])
print("2nd and 3rd column\n",s[['A2', 'A3']])
print("Last  row data\n",s.tail(1))
print("First four row data\n",s.head(4))
print("2nd row and 3rd column data:",s.loc['X2','A3'])
print("1st two col where value is >.5\n",s[['A1', 'A2']][s[['A1', 'A2']] > 0.5])
print("1st col where value is less than 0.3\n",s[s['A1'] < 0.3])


