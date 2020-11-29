"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def isTexting(texts, caller):
    for text in texts:
        sender = text[0]
        receiver = text[1]
        if caller == sender or caller == receiver:
            return True
    return False


def isReceivingCalls(calls, caller):
    for receiver in calls[1]:
        if receiver == caller:
            True
    return False


def potential_telemarketers(calls, texts):
    telemarketers = set()
    for call in calls:
        caller = call[0]
        if not isTexting(texts, caller) and not isReceivingCalls(calls, caller):
            telemarketers.add(caller)
    return telemarketers

telemarketers = potential_telemarketers(calls, texts)
print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)

# 2O(N^2)





