import pandas as pd
import numpy as np

df = pd.DataFrame({
    "EMP_ID": ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008"],
    "Age": [25, 30, 22, 28, 35, 40, 29, 31],
    "Department": ["HR", "Finance", "IT", "Marketing", "Finance", "IT", "HR", "Marketing"],
    "Salary": [50000, 60000, 45000, 55000, 70000, 65000, 52000, 58000],
    "Experience_Years": [2, 5, 1, 3, 7, 6, 4, 5],
    "Performance_Score": [85, 90, 80, 88, 92, 87, 89, 91],
    "Promotion_Eligibility": [True, True, False, True, True, False, True, True]
})

print("Employee DataFrame:")
print(df)

# salary per year of experience
df["Salary_per_Year_Experience"] = df["Salary"] / df["Experience_Years"]
print("\nEmployee DataFrame with Salary per Year of Experience:")
print(df)

# experience level categorization
def categorize_experience(years):
    if years < 3:
        return "Junior"
    elif 3 <= years < 6:
        return "Mid-level"
    else:
        return "Senior"

df["Experience_Level"] = df["Experience_Years"].apply(categorize_experience)
print("\nEmployee DataFrame with Experience Level:")
print(df)


# convert experience years into categorical data
df["Experience_Years_Cat"] = pd.cut(df["Experience_Years"], bins=[0, 2, 5, np.inf], labels=["0-2", "3-5", "6+"])
print("\nEmployee DataFrame with Experience Years Categorical:")
print(df)

#normalize salary using min-max scaling

df["Normalized_Salary"] = (df["Salary"] - df["Salary"].min()) / (df["Salary"].max() - df["Salary"].min())
print("\nEmployee DataFrame with Normalized Salary:")
print(df)