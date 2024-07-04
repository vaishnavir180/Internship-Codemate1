#Pandas-profiling For generating automatic report
import pandas as pd
data=pd.read_csv('fooddata.csv')
from Pandas_Profiling import ProfileReport
report=ProfileReport(data)
report.to_file("Data4.html")


