"""
RECORD CHECK  -  my version
===========================

Name  : Adel Gholamshahzadeh
Lane  :  AI 
Date  : 10/17/20206

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def status_of(percent,warning_at=90):
    """returns a string based on value input of percent (and warning_at if applied)"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Returns the difference and percentage"""
    difference = value - limit
    percent = (value / limit)*100
    status = status_of(percent)
    return difference, percent, status



label = input("Label: ")     # replace with an input() call
value = float(input("Value: "))   # replace with an input() call, converted
limit = float(input("Limit: "))  # replace with an input() call, converted



difference, percent,status = check(value, limit)   # replace with your code
status = status_of(percent)          # replace with your code


def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value: {value:>5.2f}")
    print(f"Limit: {limit:>5.2f}")
    print(f"Difference: {difference:>5.2f}")
    print(f"Percent: {percent:>5.2f}%")
    print(f"Status: {status}")
    print("=" * 34)





records = [] 
records.append({"label": label, "value": value, "limit": limit})  # replace with your code
print(records)

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

for x in records:
    difference, percent, status = check(x["value"], x["limit"])
    print_report(
        x["label"],
        x["value"],
        x["limit"],
        difference,
        percent,
        status
    )

over_the_limit_count = 0

if status == "OVER LIMIT":
    over_the_limit_count += 1

print(f" Total records over limit: {over_the_limit_count}")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
