import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
#plt.plot(yield_apples)

years = [2010, 2011, 2012, 2013, 2014, 2015]
sns.scatterplot(years)
plt.xlabel('Year')
plt.ylabel('Yield')
plt.show()

## Pie Chart

# A pie chart is a circular statistical graphic that is divided into slices to illustrate numerical proportions.
# Let's create a simple pie chart showing the distribution of fruit sales.

labels = ['Apples', 'Oranges', 'Bananas', 'Grapes']
sizes = [15, 30, 45, 10]  # Percentage of each fruit
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # Colors for each slice
explode = (0.1, 0, 0, 0)  # explode the 1st slice (i.e. 'Apples')

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Fruit Sales Distribution')
plt.show();

## Line Chart Example 

# Example of a simple line chart
years = [2010, 2011, 2012, 2013, 2014, 2015]
sales = [100, 150, 200, 250, 300, 350]

plt.figure(figsize=(8, 6))
plt.plot(years, sales, marker='o', color='b', linestyle='-')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show();

## Bar Chart Example

# Example of a simple bar chart
categories = ['Category A', 'Category B', 'Category C']
values = [10, 20, 15]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='orange')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show();

## Scatter Plot Example

# Example of a simple scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show();

## Histogram Example

# Example of a simple histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.figure(figsize=(8, 6))
plt.hist(data, bins=5, color='purple', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show();

## Heatmap Example

# Example of a simple heatmap

data = np.random.rand(10, 12)  # Random data
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Heatmap Example')
plt.show();
