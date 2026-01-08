import pandas as pd
import matplotlib.pyplot as plt

#Load CSV Data
df = pd.read_csv("sales_data.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

#Basic KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# Region-wise Sales Analysis
region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion-wise Sales:")
print(region_sales)

#Category-wise Profit Analysis
category_profit = df.groupby('Category')['Profit'].sum()
print("\nCategory-wise Profit:")
print(category_profit)

#Visualization - Region Sales
region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
