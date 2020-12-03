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

callers = {call[0] for call in calls}
call_receivers = {call[1] for call in calls}
texters = {text[0] for text in texts}
text_receiver = {text[1] for text in texts}

telemarketers = callers.difference(call_receivers)
telemarketers = telemarketers.difference(texters)
telemarketers = telemarketers.difference(text_receiver)


if __name__ == '__main__':
    print("These numbers could be telemarketers: ")
    telemarketers_sorted = sorted(telemarketers)
    for telemarketer in telemarketers_sorted:
        print(telemarketer)


