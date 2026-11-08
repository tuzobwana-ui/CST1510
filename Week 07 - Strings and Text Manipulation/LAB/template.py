"""
RECORD CHECK  -  my version
===========================

Name  :  Aida Tuzo Bwana
Lane  :  AI
Date  :  11/07/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

#cleans and separates one raw record
def parse_line(raw_line):
    """Clean and convert one raw dataset record into a dictionary"""
    #removes extra spaces and make all text lowecase
    parts = raw_line.strip().lower().split(",")

    #gets the dataset name, rating and age
    dataset = parts[0].strip()
    rating = int(parts[1].split("=")[1].strip())
    age = int(parts[2].split("=")[1].strip())

    #stores the clean information in a dictionary
    return{
        "dataset": dataset,
        "rating": rating,
        "age": age
    }

#this function checks the rating and gives it a status
def status_of(rating):
    """Return FLAGGED if the rating is 4 or above, otherwise OK"""
    
    #ratings of 4 or higher are flagged
    if rating >= 4:
        return "FLAGGED"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

#create an empty list to stoe the raw records
raw_records = []

#open the text file and read each line
with open("raw_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)

# =============================================================== PROCESS + OUTPUT

#start the flagged record counter at zero
flagged_count = 0

#go through each rae record in the list
for raw_record in raw_records:
    #clean and convert the rae record into a dictionary
    record = parse_line(raw_record)
    #check the rating and get its status
    status = status_of(record["rating"])

    #print the cleaned record and its status
    print(record)
    print("Status:", status)
    print()

    #add one to the counter if the record is flagged
    if status == "FLAGGED":
        flagged_count += 1

#print the final summary
print("SUMMARY")
print("Total records:", len(raw_records))
print("Flagged records:", flagged_count)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
