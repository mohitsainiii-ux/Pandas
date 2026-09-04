#seprate 1000 employee data into 10 files

import pandas as pd
import numpy as np
from pathlib import Path

# Create a sample DataFrame with 1000 rows
df = pd.DataFrame({
    "Name": [f"Employee {i}" for i in range(1000)],
    "Age": np.random.randint(20, 60, 1000),
    "Salary": np.random.randint(30000, 100000, 1000)
})

output_dir = Path(__file__).resolve().parent / "employee_files"
output_dir.mkdir(exist_ok=True)

for file_number, start in enumerate(range(0, len(df), 100), start=1):
    df.iloc[start:start + 100].to_csv(
        output_dir / f"employees_{file_number}.csv",
        index=False,
    )

print(f"Created {len(df) // 100} files in: {output_dir}")