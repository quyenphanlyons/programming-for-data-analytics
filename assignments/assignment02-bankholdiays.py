# Program that prints out the dates of the bank holidays that happen in northern Ireland.
# Author: Quyen

import json

filename = "bank-holidays.json"

with open(filename,"r") as fn:
    bh = json.load(fn)
    ni_bh = bh["northern-ireland"]["events"]
    for row in ni_bh:
       print (f"{row['date']}  {row['title']}")


# Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or the date of the holiday to decide if it is unique.