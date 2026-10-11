"""
RECORD CHECK  -  my version
===========================

Name  : Aida Tuzo Bwana
Lane  : Cyber
Date  : 11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#FUNCTION
def status_of(percent):
    """Return a status based on the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate the difference and percentage"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

#INPUT

label = input("Enter souce IP:")
value - float(input("Enter failed logins:"))
limit = float(input("Enter total attempts: "))

#PROCESS

difference, percent = check(value, limit)
status = status_of(percent)

#OUTPUT

print()
print("=" *34)
print(f"  RECORD CHECK  -  {label}")
print("=" *34)
print(f"  Failed logins : {value:>10.2f}")
print(f"  Total attempts : {value:>10.2f}")
print(f"  Other attempts : {value:>10.2f}")
print(f"  Percent : {value:>10.2f} %")
print(f"  Status : {value:>13}")
print("=" * 34)

# ==========================================================================
#Run it with a total of 0 and note the error (do not fix it yet)
#ZeroDivisionError: division by zero
