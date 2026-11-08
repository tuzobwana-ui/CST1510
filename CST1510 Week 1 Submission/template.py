"""
RECORD CHECK  -  my version
===========================

Name  : Aida Tuzo Bwana
Lane  : AI
Date  : 01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Enter dataset name: ")
first = int(input("Enter rows loaded: "))
second = int(input("Enter rows expected: "))

# ================================================================== PROCESS

# 2. Work out what you were NOT given.       [Typical and above]

difference = second - first
percent = (first / second) * 100

# =================================================================== OUTPUT

# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Loaded      : {first:>10.2f}")
print(f"  Expected    : {second:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Note        : Difference shows its sign")

print("=" * 34)

# ==========================================================================

# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
