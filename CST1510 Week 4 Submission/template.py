"""
RECORD CHECK  -  my version
===========================

Name  :  Aida Tuzo Bwana
Lane  :  AI
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return the difference, percent used and status for one value against its limit"""
    difference = limit - value
    percent = value / limit * 100
    if value > limit:
        status = "OVER LIMIT"
    elif percent >= 80:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print one formatted report block for a single record"""
    print(f"--- {label} ---")
    print(f"Used      : {value} GB of {limit} GB")
    print(f"Remaining : {difference} GB")
    print(f"Percent   : {percent:.1f}%")
    print(f"Status    : {status}")
    print()

def load_records(path):
    """Read label, value, limit lines from a file and return a list of dictionaries"""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records

def save_results(path, results):
    """Write one label, status line per result to a new file"""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label}, {status}\n")

# ====================================================================== STORE

try:
    records = load_records("data.txt")
except FileNotFoundError:
    print("Could not find data.txt. Starting with an empty list.")
    records = []

# =============================================================== PROCESS + OUTPUT
results = []
over_count = 0

for record in records:
    difference, percent, status = check_record([record["value"], record["limit"]])
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)
    results.append((record["label", status]))
    if status == "OVER LIMIT":
        over_count += 1

save_results("results.txt,", results)
print(f"Record over limit: {over_count}")

