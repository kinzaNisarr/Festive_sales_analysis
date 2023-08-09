# import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Check the shape of the dataframe
df.shape

# Display the first few rows of the dataframe
df.head()

# Display information about the dataframe
df.info()

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
pd.isnull(df).sum()

# Drop rows with null values
df.dropna(inplace=True)

# Change data type of the 'Amount' column from float to integer
df['Amount'] = df['Amount'].astype('int')

# Rename the 'Marital_Status' column to 'Shaadi'
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Display basic statistics of age, order, and amount columns
df[['Age', 'Orders', 'Amount']].describe()

# Plotting a bar chart for Gender and its count
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting a bar chart for Gender vs Total Amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen)

# Plotting a bar chart for Age Group and its count
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting a bar chart for Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)

# Plotting total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')

# Plotting total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(data=sales_state, x='State', y='Amount')

# Plotting a bar chart for Marital Status and its count
ax = sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(7, 5)})
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting sales by Marital Status and Gender
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6, 5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')

# Plotting a bar chart for Occupation and its count
sns.set(rc={'figure.figsize':(20, 5)})
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting sales by Occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')

# Plotting a bar chart for Product Category and its count
sns.set(rc={'figure.figsize':(20, 5)})
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)

# Plotting sales by Product Category
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')

# Plotting sales by Product ID
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')

# Plotting top 10 most sold products using a bar chart
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
