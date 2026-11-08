"""
RECORD CHECK  -  my version
===========================

Name  :  Aida Tuzo Bwana
Lane  :  AI
Date  :  01/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("datasets.csv")   # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.

print("Full DataFrame")
print(df)
#outputs the full dataframe

print("\nRows That Are Not Ok")
print(df[df["status"] != "OK"])
#outputs the rows which are not ok

print("\nCount Per Status")
print(df.groupby("status").size())
#group by status and counts each group

df.to_csv("datasets_report.csv", index=False)
#saves the dataframe

#Create and save bar chart
import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind="bar")
plt.title("Dataset Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_counts.png")
plt.show()

# ==========================================================================
