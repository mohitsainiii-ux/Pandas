import pandas as pd
import numpy as np

df = pd.DataFrame({
    "OrderID" : [
        "0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009", "0010","0011", "0012", "0013", "0014", "0015"
    ],

    "Date" : [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10","2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15"
    ],

    "Region" : [
        "North", "South", "East", "West", "North", "South", "East", "West", "North", "South","East", "West", "North", "South", "East"
    ],

    "Product" : [
        "Product A", "Product B", "Product C", "Product D", "Product A", "Product B", "Product C", "Product D", "Product A", "Product B","Product C", "Product D", "Product A", "Product B", "Product C"
    ],
    "Quantity" : [
        10, 20, 15, 30, 25, 10, 20, 15, 30, 25,10, 20, 15, 30, 25
    ],

    "UnitPrice" : [
        100, 200, 150, 300, 250, 100, 200, 150, 300, 250,100, 200, 150, 300, 250
    ],

    "TotalPrice" : [
        1000, 4000, 2250, 9000, 6250, 1000, 4000, 2250, 9000, 6250,1000, 4000, 2250, 9000, 6250
    ]
})

#convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df)

#create revenue column by multiplying Quantity and UnitPrice
df['Revenue'] = df['Quantity'] * df['UnitPrice']
print(df)

#create a new column 'Profit' by subtracting TotalPrice from Revenue
df['Profit'] = df['Revenue'] - df['TotalPrice']
print(df)

#create a new column 'ProfitMargin' by dividing Profit by Revenue and multiplying by 100
df['ProfitMargin'] = (df['Profit'] / df['Revenue']) * 100
print(df)

#create a new column 'CumulativeRevenue' by calculating the cumulative sum of Revenue
df['CumulativeRevenue'] = df['Revenue'].cumsum()
print(df)

#total revenue for each region
total_revenue_region = df.groupby('Region')['Revenue'].sum().reset_index()
print(total_revenue_region)
