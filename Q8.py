import pandas as pd
import numpy as np
customers = pd.DataFrame({
    "Customer_ID": [
        "C001", "C002", "C003",
        "C004", "C005", "C006"
    ],

    "Name": [
        "Rahul", "Aman", "Priya",
        "Neha", "Vikas", "Riya"
    ],

    "City": [
        "Jaipur", "Delhi", "Mumbai",
        "Jaipur", "Pune", "Delhi"
    ]
})


#order
orders = pd.DataFrame({
    "Order_ID": [
        "O1001", "O1002", "O1003",
        "O1004", "O1005", "O1005",
        "O1006", "O1007"
    ],

    "Customer_ID": [
        "C001", "C002", "C003",
        "C004", "C005", "C005",
        "C006", "C007"
    ],

    "Amount": [
        5000, 7000, 4500, 8000,
        6500, 6500, np.nan, 9000
    ],

    "Status": [
        "Completed", "Completed", "Pending",
        "Completed", "Completed", "Completed",
        "Completed", "Completed"
    ]
})

#payment
payments = pd.DataFrame({
    "Payment_ID": [
        "P001", "P002", "P003", "P004",
        "P005", "P006", "P007"
    ],

    "Order_ID": [
        "O1001", "O1002", "O1003",
        "O1004", "O1005", "O1006", "O1008"
    ],

    "Paid_Amount": [
        5000, 7000, 4500, 8000,
        6500, 6000, 3000
    ],

    "Payment_Status": [
        "Paid", "Paid", "Paid", "Paid",
        "Paid", "Partial", "Paid"
    ]
})

duplicate_orders = orders[
    orders.duplicated(
        subset="Order_ID",
        keep=False
    )
]

print("Duplicate Orders:")
print(duplicate_orders)



orders = orders.drop_duplicates(
    subset="Order_ID",
    keep="first"
)


invalid_customers = orders[
    ~orders["Customer_ID"].isin(
        customers["Customer_ID"]
    )
]

print("\nInvalid Customers:")
print(invalid_customers)

print("\nMissing Values:")
print(orders.isna().sum())


median_amount = orders["Amount"].median()

orders["Amount"] = orders["Amount"].fillna(
    median_amount
)

df = orders.merge(
    customers,
    on="Customer_ID",
    how="left"
)


df = df.merge(
    payments,
    on="Order_ID",
    how="left"
)


df["Paid_Amount"] = df["Paid_Amount"].fillna(0)


df["Payment_Difference"] = (
    df["Amount"] -
    df["Paid_Amount"]
)

conditions = [
    df["Paid_Amount"] == 0,

    df["Paid_Amount"] ==
    df["Amount"],

    df["Paid_Amount"] <
    df["Amount"],

    df["Paid_Amount"] >
    df["Amount"]
]

choices = [
    "Not Paid",
    "Fully Paid",
    "Partially Paid",
    "Overpaid"
]

df["Payment_Status_Final"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

not_fully_paid = df[
    df["Payment_Status_Final"] !=
    "Fully Paid"
]

print("\nNot Fully Paid:")
print(not_fully_paid)


total_orders = df["Amount"].sum()

total_paid = df["Paid_Amount"].sum()

outstanding = (
    df["Amount"] -
    df["Paid_Amount"]
).sum()

print("\nFinancial Summary:")
print("Total Orders:", total_orders)
print("Total Paid:", total_paid)
print("Outstanding:", outstanding)

customer_sales = (
    df[df["Name"].notna()]
    .groupby("Customer_ID")["Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)

top_customer = customer_sales.idxmax()

top_customer_value = customer_sales.max()

print("\nTop Customer:")
print("Customer:", top_customer)
print("Order Value:", top_customer_value)

no_payment = df[
    df["Paid_Amount"] == 0
]

print("\nOrders With No Payment:")
print(
    no_payment[
        [
            "Order_ID",
            "Customer_ID",
            "Name"
        ]
    ]
)

final_report = df[
    [
        "Order_ID",
        "Customer_ID",
        "Name",
        "City",
        "Amount",
        "Paid_Amount",
        "Payment_Difference",
        "Payment_Status_Final"
    ]
]

print("\nFinal Report:")
print(final_report)