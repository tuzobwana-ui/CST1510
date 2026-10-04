"""
RECORD CHECK  -  my version
===========================

Name  : Aida Tuzo Bwana
Lane  : IT      
Date  : 09/10/2026

Run it:   python template.py

"""

over_limit_count = 0   # how many records came back OVER LIMIT this session

while True:
    hostname = input("Enter hostname (or 'quit' to stop): ")
    if hostname.lower() == "quit":
        break

    gb_used = float(input("Enter GB used: "))
    gb_total = float(input("Enter GB total: "))

    # ============================================================== PROCESS
    gb_free = gb_total - gb_used
    percent_used = gb_used / gb_total * 100

    if percent_used >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent_used >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used        : {gb_used:>10.2f}")
    print(f"  Total       : {gb_total:>10.2f}")
    print(f"  Free        : {gb_free:>10.2f}")
    print(f"  Percent     : {percent_used:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print()
print(f"Records OVER LIMIT this session: {over_limit_count}")