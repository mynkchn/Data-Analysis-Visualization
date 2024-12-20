import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

candy_products=pd.read_csv('Candy_Products.csv')
print(candy_products)
print(candy_products.columns)
print(candy_products.shape)
print(candy_products.info())
print(candy_products.describe())

candy_products.set_index(candy_products['Division'],inplace=True)

candy_products.plot(label='Candy Products', color='blue,green')
plt.title('Information regarding candy Products')
plt.xlabel('Divisions')
plt.ylabel(candy_products.columns)
plt.legend()
plt.show()


