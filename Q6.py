import pandas as pd

# Dataset
sales = pd.DataFrame({
    "Date": [
        "2026-01-05",
        "2026-01-12",
        "2026-01-20",
        "2026-02-03",
        "2026-02-15",
        "2026-02-25",
        "2026-03-02",
        "2026-03-15",
        "2026-03-20",
        "2026-03-28",
        "2026-04-05",
        "2026-04-18"
    ],

    "Sales": [
        50000,
        65000,
        55000,
        70000,
        80000,
        75000,
        90000,
        95000,
        85000,
        100000,
        110000,
        120000
    ]
})


# Q1: Convert Date
sales["Date"] = pd.to_datetime(sales["Date"])


# Q2: Create Month
sales["Month"] = sales["Date"].dt.to_period("M")


# Q3: Monthly Sales
monthly_sales = (
    sales.groupby("Month")["Sales"]
         .sum()
)

print("Monthly Sales:")
print(monthly_sales)


# Q4: Sales Difference
monthly_sales_diff = monthly_sales.diff()

print("\nSales Difference:")
print(monthly_sales_diff)


# Q5: Growth Percentage
monthly_growth = (
    monthly_sales.pct_change() * 100
)

print("\nGrowth Percentage:")
print(monthly_growth)


# Q6: Highest Sales Month
best_month = monthly_sales.idxmax()
best_sales = monthly_sales.max()

print("\nBest Month:", best_month)
print("Best Sales:", best_sales)


# Q7: Biggest Increase
biggest_increase_month = (
    monthly_sales_diff.idxmax()
)

biggest_increase = monthly_sales_diff.max()

print("\nBiggest Increase Month:",
      biggest_increase_month)

print("Biggest Increase:",
      biggest_increase)


# Q8: 3-Month Rolling Average
rolling_avg = (
    monthly_sales
    .rolling(window=3)
    .mean()
)

print("\n3-Month Rolling Average:")
print(rolling_avg)


# Q9 + Q10: Final Analysis DataFrame
monthly_df = (
    sales.groupby("Month", as_index=False)["Sales"]
         .sum()
)

monthly_df["Sales_Difference"] = (
    monthly_df["Sales"].diff()
)

monthly_df["Growth_Percentage"] = (
    monthly_df["Sales"].pct_change() * 100
)

monthly_df["Rolling_3M_Average"] = (
    monthly_df["Sales"]
    .rolling(window=3)
    .mean()
)

print("\nFinal Monthly Analysis:")
print(monthly_df)