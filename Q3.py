import pandas as pd

# Employees
employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Vikas", "Riya"],
    "Dept_ID": [1, 2, 1, 3, 2, 4],
    "Salary": [50000, 60000, 55000, 70000, 65000, 45000]
})

# Departments
departments = pd.DataFrame({
    "Dept_ID": [1, 2, 3],
    "Department": ["IT", "HR", "Finance"],
    "Manager": ["Raj", "Simran", "Karan"]
})

# Performance
performance = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 105, 106],
    "Rating": [4.5, 3.8, 4.2, 4.8, 3.5],
    "Projects": [5, 3, 4, 6, 2]
})


# 1. Merge Employees + Departments
df = employees.merge(
    departments,
    on="Dept_ID",
    how="left"
)


# 2. Merge with Performance
df = df.merge(
    performance,
    on="Emp_ID",
    how="left"
)


# 3. Check missing values
print("Missing Values:")
print(df.isna().sum())


# 4. Fill missing values
df["Department"] = df["Department"].fillna("Unknown")
df["Manager"] = df["Manager"].fillna("Not Assigned")

df["Rating"] = df["Rating"].fillna(0)
df["Projects"] = df["Projects"].fillna(0)


# 5. Performance Score
df["Performance_Score"] = (
    df["Rating"] * df["Projects"]
)


# 6. Highest Performance Score
best_employee = df.loc[
    df["Performance_Score"].idxmax(),
    ["Name", "Department", "Rating",
     "Projects", "Performance_Score"]
]

print("\nBest Employee:")
print(best_employee)


# 7. Average Salary by Department
avg_salary = (
    df.groupby("Department")["Salary"]
      .mean()
)

print("\nAverage Salary:")
print(avg_salary)


# 8. Salary > 55000 AND Rating >= 4
filtered = df[
    (df["Salary"] > 55000) &
    (df["Rating"] >= 4.0)
]

print("\nFiltered Employees:")
print(filtered)


# 9. Sort by Performance Score
df = df.sort_values(
    by="Performance_Score",
    ascending=False
)

print("\nFinal DataFrame:")
print(df)