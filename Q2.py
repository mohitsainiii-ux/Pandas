import pandas as pd

df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales", "IT", "HR"],
    "Salary": [50000, 75000, 45000, 60000, 40000, 55000, 90000, 70000],
    "Experience": [2, 5, 1, 4, 1, 3, 7, 6]
})

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

df["Department_Avg_Salary"] = (
    df.groupby("Department")["Salary"].transform("mean")
)
print(df)

df["Salary_Difference"] = (
    df["Salary"] - df["Department_Avg_Salary"]
)
print(df)

above_average = df[
    df["Salary"] > df["Department_Avg_Salary"]
]
print(above_average)

top_2 = (
    df.sort_values("Salary", ascending=False)
      .groupby("Department")
      .head(2)
)
print(top_2)

df["Salary_Rank"] = (
    df["Salary"]
    .rank(ascending=False, method="dense")
)
print(df)

df = df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
)
print(df)