"""
RECORD CHECK  -  my version
===========================

Name  :  Aida Tuzo Bwana
Lane  :  AI
Date  :  23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    def __init__(self, label, value, limit):
        """Store the dataset details"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status of the dataset"""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.

r1 = Record("survey_2026", 1187, 1200)
r2 = Record("survey_2026", 1250, 1200)
records = [r1, r2]


# ==================================================================== OUTPUT
# 3. Print a report for each record.

over_limit_count = 0
for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f" Rows loaded : {record.value}")
    print(f" Rows ecpected : {record.limit}")
    print(f" Status : {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print("Records OVER LIMIT:", over_limit_count)


# ==========================================================================
# 4. Before you finish:

r1.value = 1190
print()
print("Checking independent records:")
print(r1.label, r1.value)
print(r2.label, r2.value)
