import pandas as pd
import numpy as np

# --------------------------------
# Create Dataset
# --------------------------------

df = pd.DataFrame({
    "Employee_ID": [
        101, 102, 103, 104, 105,
        105, 106, 107, 108, 109
    ],

    "Name": [
        "Rahul", "AMAN", "Priya", "neha", "Vikas",
        "Vikas", "Riya", "ARJUN", "Karan", "Meena"
    ],

    "Department": [
        "IT", "hr", "IT", "Finance", "Sales",
        "Sales", "HR", "it", "Finance", "Sales"
    ],

    "Salary": [
        50000, 60000, np.nan, 70000, 45000,
        45000, 55000, 90000, 1200000, 50000
    ],

    "Experience": [
        2, 3, 4, np.nan, 1,
        1, 3, 7, 8, 2
    ]
})


# --------------------------------
# Q1 & Q2: Find and remove duplicates
# --------------------------------

duplicates = df[
    df.duplicated(
        subset="Employee_ID",
        keep=False
    )
]

print("Duplicates:")
print(duplicates)

df = df.drop_duplicates(
    subset="Employee_ID",
    keep="first"
)


# --------------------------------
# Q3: Missing values
# --------------------------------

print("\nMissing Values:")
print(df.isna().sum())


# --------------------------------
# Q4: Fill missing Salary
# --------------------------------

df["Salary"] = (
    df.groupby("Department")["Salary"]
      .transform(
          lambda x: x.fillna(x.median())
      )
)


# --------------------------------
# Q5: Fill missing Experience
# --------------------------------

df["Experience"] = (
    df.groupby("Department")["Experience"]
      .transform(
          lambda x: x.fillna(x.median())
      )
)


# --------------------------------
# Q6: Standardize Names
# --------------------------------

df["Name"] = df["Name"].str.title()


# --------------------------------
# Q7: Standardize Department
# --------------------------------

df["Department"] = df["Department"].str.upper()


# --------------------------------
# Q8: Detect Salary Outliers
# --------------------------------

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower_bound) |
    (df["Salary"] > upper_bound)
]

print("\nSalary Outliers:")
print(outliers)


# --------------------------------
# Q9: Salary Level
# --------------------------------

conditions = [
    df["Salary"] >= 100000,
    df["Salary"] >= 60000
]

choices = [
    "High",
    "Medium"
]

df["Salary_Level"] = np.select(
    conditions,
    choices,
    default="Low"
)


# --------------------------------
# Q10: Experience Level
# --------------------------------

conditions = [
    df["Experience"] >= 5,
    df["Experience"] >= 3
]

choices = [
    "Senior",
    "Mid"
]

df["Experience_Level"] = np.select(
    conditions,
    choices,
    default="Junior"
)


# --------------------------------
# Q11: Salary Per Experience
# --------------------------------

df["Salary_Per_Year"] = (
    df["Salary"] / df["Experience"]
)


# --------------------------------
# Q12: IT employees > 60000
# --------------------------------

result = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 60000)
]

print("\nIT Employees with Salary > 60000:")
print(result)


# --------------------------------
# Q13: Sort by Salary
# --------------------------------

df = df.sort_values(
    by="Salary",
    ascending=False
)
print("\nFinal DataFrame:")
print(df)