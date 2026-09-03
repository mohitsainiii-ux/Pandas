import pandas as pd

# -----------------------------
# Create Dataset
# -----------------------------

sales = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004, 1005,
                 1006, 1007, 1008, 1009, 1010],

    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-20",
        "2026-02-03", "2026-02-15", "2026-02-25",
        "2026-03-02", "2026-03-15", "2026-03-20",
        "2026-03-28"
    ],

    "Customer": [
        "Rahul", "Aman", "Rahul", "Priya", "Aman",
        "Vikas", "Priya", "Rahul", "Vikas", "Aman"
    ],

    "Product": [
        "Laptop", "Mouse", "Keyboard", "Laptop",
        "Monitor", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Keyboard"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories",
        "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Electronics",
        "Accessories"
    ],

    "Quantity": [2, 5, 3, 1, 2, 10, 4, 1, 2, 6],

    "Price": [
        60000, 800, 1500, 62000, 15000,
        750, 1400, 14500, 61000, 1300
    ]
})


# -----------------------------
# Q1. Convert Date
# -----------------------------

sales["Date"] = pd.to_datetime(sales["Date"])


# -----------------------------
# Q2. Total Sales
# -----------------------------

sales["Total_Sales"] = (
    sales["Quantity"] * sales["Price"]
)


# -----------------------------
# Create Month
# -----------------------------

sales["Month"] = sales["Date"].dt.to_period("M")


# -----------------------------
# Q3. Monthly Sales
# -----------------------------

monthly_sales = (
    sales.groupby("Month")["Total_Sales"]
         .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)


# -----------------------------
# Q4. Category Sales
# -----------------------------

category_sales = (
    sales.groupby("Category")["Total_Sales"]
         .sum()
)

print("\nCategory Sales:")
print(category_sales)


# -----------------------------
# Q5. Top 3 Customers
# -----------------------------

customer_sales = (
    sales.groupby("Customer")["Total_Sales"]
         .sum()
         .sort_values(ascending=False)
)

print("\nTop 3 Customers:")
print(customer_sales.head(3))


# -----------------------------
# Q6. Best-Selling Product
# -----------------------------

product_quantity = (
    sales.groupby("Product")["Quantity"]
         .sum()
         .sort_values(ascending=False)
)

best_product = product_quantity.idxmax()

print("\nBest-Selling Product:")
print(best_product)


# -----------------------------
# Q7. Customer Contribution %
# -----------------------------

customer_percentage = (
    customer_sales / sales["Total_Sales"].sum()
) * 100

print("\nCustomer Contribution:")
print(customer_percentage)


# -----------------------------
# Q8. Highest-Value Order
# -----------------------------

highest_order = sales.loc[
    sales["Total_Sales"].idxmax(),
    ["Order_ID", "Customer",
     "Product", "Total_Sales"]
]

print("\nHighest Value Order:")
print(highest_order)


# -----------------------------
# Q9. Category Summary
# -----------------------------

category_summary = (
    sales.groupby("Category")
         .agg(
             Total_Sales=("Total_Sales", "sum"),
             Average_Sales=("Total_Sales", "mean"),
             Total_Quantity=("Quantity", "sum"),
             Number_of_Orders=("Order_ID", "count")
         )
)

print("\nCategory Summary:")
print(category_summary)


# -----------------------------
# Q10. Pivot Table
# -----------------------------

pivot = pd.pivot_table(
    sales,
    values="Total_Sales",
    index="Category",
    columns="Month",
    aggfunc="sum",
    fill_value=0
)

print("\nCategory × Month:")
print(pivot)