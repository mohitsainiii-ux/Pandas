import pandas as pd

orders = pd.DataFrame({
    "Order_ID": [
        "O1001", "O1002", "O1003",
        "O1004", "O1005", "O1006",
        "O1007", "O1008", "O1009",
        "O1010", "O1011", "O1012",
        "O1013", "O1014", "O1015"
    ],
    "Customer": [
        "Aman", "Ravi", "Priya",
        "Amit", "Neha","Sonal",
        "Rohit", "Anjali", "Karan",
        "Simran", "Vikram", "Pooja",
        "Aarav", "Isha", "Kabir"
    ],
    "Order_Date": [
        "2023-01-15", "2023-01-20", "2023-02-05",
        "2023-02-10", "2023-03-01", "2023-03-15",
        "2023-04-01", "2023-04-10", "2023-05-05",
        "2023-05-15", "2023-06-01", "2023-06-10",
        "2023-07-05", "2023-07-15", "2023-08-01"
    ],
    "Amount": [
        1200, 800, 300, 150, 200, 500,
        100, 250, 400, 600, 700, 900,
        1100, 1300, 1400
    ],
})

#covert date into datetime format
orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])
print("Orders DataFrame:")
print(orders)

#create a Month column
orders["Month"] = orders["Order_Date"].dt.month
print("\nOrders DataFrame with Month Column:")
print(orders)

#find each customers first purchase month
first_purchase_month = orders.groupby("Customer")["Month"].min().reset_index()
first_purchase_month.rename(columns={"Month": "First_Purchase_Month"}, inplace=True)
print("\nFirst Purchase Month for Each Customer:")
print(first_purchase_month)

#calculate monthly active customers
monthly_active_customers = orders.groupby("Month")["Customer"].nunique().reset_index()
print("\nMonthly Active Customers:")
print(monthly_active_customers)

#calculate total sales by month
total_sales_by_month = orders.groupby("Month")["Amount"].sum().reset_index()
print("\nTotal Sales by Month:")
print(total_sales_by_month)

#createa cohort analysis by month
cohort_analysis = orders.groupby(["Month", "Customer"]).size().reset_index(name="Orders_Count")
print("\nCohort Analysis by Month:")
print(cohort_analysis)