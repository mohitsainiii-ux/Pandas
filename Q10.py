import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "Order_ID": [
        "O1001", "O1002", "O1003",
        "O1004", "O1005", "O1006",
        "O1007", "O1008"
    ],
    "Customer_ID": [
        "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"
    ],
    "Product": [
        "Laptop", "Smartphone", "Tablet",
        "Headphones", "Smartwatch", "Camera",
        "Printer", "Monitor"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories", "Electronics",
        "Accessories", "Electronics"
    ],
    "Region": [
        "North", "South", "East", "West",
        "North", "South", "East", "West"
    ],
    "Quantity": [
        2, 1, 3, 5, 2, 1, 4, 2
    ],
    "Price": [
        1200, 800, 300, 150, 200, 500, 100, 250
    ],
    "Order_Date": [
        "2023-01-15", "2023-01-20", "2023-02-05",
        "2023-02-10", "2023-03-01", "2023-03-15",
        "2023-04-01", "2023-04-10"
    ]
})

print("Sales DataFrame:")
print(sales)

#calculate total sales for each order
sales["Total_Sales"] = sales["Quantity"] * sales["Price"]
print("\nSales DataFrame with Total Sales:")
print(sales)

#convert date into datetime format
sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])
print("\nSales DataFrame with Converted Dates:")
print(sales)

#find total sales by category
total_sales_by_category = sales.groupby("Category")["Total_Sales"].sum().reset_index()
print("\nTotal Sales by Category:")
print(total_sales_by_category)

#find total sales by region
total_sales_by_region = sales.groupby("Region")["Total_Sales"].sum().reset_index()
print("\nTotal Sales by Region:")
print(total_sales_by_region)

#create multiindex summary
multiindex_summary = sales.groupby(["Category", "Region"])["Total_Sales"].sum().reset_index()
print("\nMultiIndex Summary of Total Sales by Category and Region:")
print(multiindex_summary)

#create a pivot table for total sales by category and region
pivot_table = sales.pivot_table(values="Total_Sales", index="Category", columns="Region", aggfunc=np.sum, fill_value=0)
print("\nPivot Table of Total Sales by Category and Region:")
print(pivot_table)