import pandas as pd

df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "Salary": [50000, 45000, 70000, 40000, 55000, 65000],
    "Experience": [2, 1, 5, 1, 3, 4]
})

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

highest_salary = df.loc[
    df.groupby("Department")["Salary"].idxmax()
]
print(highest_salary)

df["Salary_Per_Experience"] = df["Salary"] / df["Experience"]
print(df)

filtered_df = df[
    (df["Salary"] > 50000) &
    (df["Experience"] >= 3)
]
print(filtered_df)

sorted_df = df.sort_values(
    by="Salary_Per_Experience",
    ascending=False
)
print(sorted_df)