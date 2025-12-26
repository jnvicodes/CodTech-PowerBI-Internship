# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Total, Profit Margin, Product Category)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import matplotlib.pyplot as plt

# Remove missing values
df = dataset.dropna()

# Scatter plot: Sales vs Profit
plt.figure(figsize=(8,5))
plt.scatter(df['Total'], df['Profit Margin'], alpha=0.6)

plt.xlabel('Total Sales')
plt.ylabel('Profit')
plt.title('Sales vs Profit Analysis (Python)')

plt.show()
