import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2023-01-15", "2023-01-20", "2023-02-05",
        "2023-02-10", "2023-03-01", "2023-03-15",
        "2023-04-01", "2023-04-10"
    ],
    "SalesPerson": [
        "Amit", "Neha", "Rohit",
        "Simran", "Vikram", "Pooja",
        "Aarav", "Isha"
    ],
    "Region": [
        "North", "South", "East",
        "West", "North", "South",
        "East", "West"
    ],
    "sales": [
        1200, 800, 300, 150, 200, 500, 100, 250
    ]
})

# date into datetime format
df["Date"] = pd.to_datetime(df["Date"])
print("Sales DataFrame:")
print(df)

# total sales for each salesperson
total_sales_by_salesperson = df.groupby("SalesPerson")["sales"].sum().reset_index()
print("\nTotal Sales by SalesPerson:")
print(total_sales_by_salesperson)

# calculate each salesperson's contribution to total sales
total_sales = df["sales"].sum()
df["Contribution"] = (df["sales"] / total_sales) * 100
print("\nSales DataFrame with Contribution:")
print(df)

# add a column
df["Cumulative_Sales"] = df.groupby("SalesPerson")["sales"].cumsum()
print("\nSales DataFrame with Cumulative Sales:")
print(df)

# salesperson average sales

average_sales_by_salesperson = df.groupby("SalesPerson")["sales"].mean().reset_index()
print("\nAverage Sales by SalesPerson:")
print(average_sales_by_salesperson)

# create a pivot table to summarize sales by region and salesperson
pivot_table = df.pivot_table(values="sales", index="Region", columns="SalesPerson", aggfunc="sum", fill_value=0)
print("\nPivot Table of Sales by Region and SalesPerson:")
print(pivot_table)