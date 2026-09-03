import pandas as pd
import numpy as np

orders = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
    "Customer" : ["Mohit", "Anjali", "Rohit", "Priya", "Amit", "Sneha", "Vikram", "Kavita", "Rahul", "Pooja", "Sanjay", "Neha"],
    "Order_Date": pd.to_datetime([
        "2023-01-15", "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
        "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25", "2023-01-26"
    ]),
    "Amount":[
        50000, 15000, 55000, 70000, 80000, 75000, 90000, 95000, 85000, 100000, 110000, 120000
    ]
})

#convert date
orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])

#Build RFM Table

rfm = orders.groupby("Customer").agg({
    "Order_Date": lambda x: (orders["Order_Date"].max() - x.max()).days,
    "Order_ID": "count",
    "Amount": "sum"
}).rename(columns={
    "Order_Date": "Recency",
    "Order_ID": "Frequency",
    "Amount": "Monetary"
})

#Custommer Segmentation

conditions = [
    (rfm["Recency"] <= 30) & (rfm["Frequency"] >= 2) & (rfm["Monetary"] >= 50000),
    (rfm["Recency"] <= 30) & (rfm["Frequency"] < 2) & (rfm["Monetary"] >= 50000),
    (rfm["Recency"] > 30) & (rfm["Frequency"] >= 2) & (rfm["Monetary"] >= 50000),
    (rfm["Recency"] > 30) & (rfm["Frequency"] < 2) & (rfm["Monetary"] >= 50000),
    (rfm["Recency"] <= 30) & (rfm["Frequency"] >= 2) & (rfm["Monetary"] < 50000),
    (rfm["Recency"] <= 30) & (rfm["Frequency"] < 2) & (rfm["Monetary"] < 50000),
    (rfm["Recency"] > 30) & (rfm["Frequency"] >= 2) & (rfm["Monetary"] < 50000),
    (rfm["Recency"] > 30) & (rfm["Frequency"] < 2) & (rfm["Monetary"] < 50000)
]

print("RFM Table:")
print(rfm)

print("\nCustomer Segmentation:")
for i, condition in enumerate(conditions):
    segment = rfm[condition]
    print(f"Segment {i+1}:")
    print(segment)
    print()