import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

complete_data=pd.read_csv('uszips.csv')
print(complete_data.columns)
print(complete_data.shape)
print(complete_data.info())
print(complete_data.describe())

candy_sales=pd.read_csv('Candy_Sales.csv')
print(candy_sales.columns)
candy_sales['state_id']=complete_data.state_id
print(candy_sales)
bundle_data=candy_sales.merge(complete_data,on='state_id')
print(bundle_data.info())
print(bundle_data.describe())
print(bundle_data.shape)
