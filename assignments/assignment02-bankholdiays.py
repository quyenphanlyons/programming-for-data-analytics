# Program that prints out the dates of the bank holidays that happen in northern Ireland.
# Author: Quyen

import json

filename = "bank-holidays.json"

with open(filename,"r") as fn:
    bh = json.load(fn)
    ni_bh = bh["northern-ireland"]["events"]
    print ("Northern Ireland Bank holidays:\n")
    for event in ni_bh:
       print (f"{event['date']}  {event['title']}")

# Modify the program to print the bank holidays that are unique to northern Ireland 
# (i.e. do not happen elsewhere in the UK) you can choose if you want to use 
# the name or the date of the holiday to decide if it is unique.

import json

import json

filename = "bank-holidays.json"

with open(filename,"r") as fn:
    bh = json.load(fn)
    ni = bh["northern-ireland"]["events"]
    ew = bh["england-and-wales"]["events"]
    sc = bh["scotland"]["events"]
    countew = len(ew)
    countsc = len(sc)
    print(countew)
    print(countsc)
    not_ir = {event["date"] for event in ew} | {event["date"] for event in sc}
    count_not_ir = len(not_ir)
    print(count_not_ir)
    print ("Bank holidays that are unique in Northern Ireland:\n")
    for event in ni:
        if event["date"] not in not_ir:
            print (f"{event['date']}  {event['title']}")
