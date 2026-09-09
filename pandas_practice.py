import pandas as pd

# 1. Load a CSV file
# df = pd.read_csv("data.csv")
# print(df.head())

# 2. Check missing values
# df = pd.read_csv("data.csv")
# print(df.isnull().sum())

# 3. Drop rows with missing values
# df = pd.read_csv("data.csv")
# df = df.dropna()
# print(df)

# 4. Filter rows based on a condition
# df = pd.read_csv("data.csv")
# filtered_df = df[df["Age"] > 30]
# print(filtered_df)

# 5. Group by and calculate average
# df = pd.read_csv("data.csv")
# avg_salary = df.groupby("Department")["Salary"].mean()
# print(avg_salary)

# Sample data for quick practice
sample_data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Department": ["HR", "IT", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 80000],
}

df = pd.DataFrame(sample_data)
print("Sample DataFrame:")
print(df)

print("\nMissing values count:")
print(df.isnull().sum())

print("\nFilter Age > 30:")
print(df[df["Age"] > 30])

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nDrop rows with missing values: ")
df_cleaned = df.dropna()
print(df_cleaned)
