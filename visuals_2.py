# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Product Category, Profit Margin)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:import pandas as pd
import matplotlib.pyplot as plt

# Clean data
df = dataset.dropna()

# Group by category and calculate average profit
grouped = df.groupby('Product Category')['Profit Margin'].mean()

# Plot bar chart
plt.figure(figsize=(8,5))
grouped.plot(kind='bar')

plt.xlabel('Product Category')
plt.ylabel('Average Profit')
plt.title('Average Profit by Product Category (Python)')

plt.tight_layout()
plt.show()
