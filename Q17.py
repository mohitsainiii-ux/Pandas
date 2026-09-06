import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Order_ID" : [
        "0001", "0002", "0003", "0004", "0005",
        "0006", "0007", "0008", "0009", "0010",
        "0011", "0012", "0013", "0014", "0015",
        "0016", "0017", "0018", "0019", "0020"
    ],

    "Date" : [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
        "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
        "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
        "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20"
    ],

    "Customer" : [
        "Customer A", "Customer B", "Customer C", "Customer D", "Customer E",
        "Customer F", "Customer G", "Customer H", "Customer I", "Customer J",
        "Customer K", "Customer L", "Customer M", "Customer N", "Customer O",
        "Customer P", "Customer Q", "Customer R", "Customer S", "Customer T"
    ],

    "Region" : [
        "North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South",
        "East", "West", "North", "South", "East",
        "West", "North", "South", "East", "West"
    ],

    "Category" : [
        "Category A", "Category B", "Category C", "Category D", "Category A",
        "Category B", "Category C", "Category D", "Category A", "Category B",
        "Category C", "Category D", "Category A", "Category B", "Category C",
        "Category D", "Category A", "Category B", "Category C", "Category D"
    ],

    "Product" : [
        "Product A", "Product B", "Product C", "Product D", "Product A",
        "Product B", "Product C", "Product D", "Product A", "Product B",
        "Product C", "Product D", "Product A", "Product B", "Product C",
        "Product D", "Product A", "Product B", "Product C", "Product D"
    ],

    "Quantity" : [
        10, 20, 15, 30, 25,
        10, 20, 15, 30, 25,
        10, 20, 15, 30, 25,
        10, 20, 15, 30, 25
    ],

    "Unit_Price" : [
        100, 200, 150, 300, 250,
        100, 200, 150, 300, 250,
        100, 200, 150, 300, 250,
        100, 200, 150, 300, 250
    ]
})

#Date Processing  year, month, month name
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()

print(df)


#calculate revenue by multiplying Quantity and Unit_Price
df['Revenue'] = df['Quantity'] * df['Unit_Price']
print(df)

#customer level analysis
customer_analysis = df.groupby('Customer').agg({
    'Revenue': 'sum',
    'Quantity': 'sum'
})
print(customer_analysis)

#customer revenue contribution percentage
total_revenue = df['Revenue'].sum()
customer_contribution = (customer_analysis['Revenue'] / total_revenue) * 100
print(customer_contribution)