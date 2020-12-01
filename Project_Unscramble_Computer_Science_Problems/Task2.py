"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def time_spent_number(calls):
    time_spent = {}
    for call in calls:
        caller = call[0]
        receiver = call[1]
        duration = call[3]
        time_spent[caller] = time_spent.get(caller, 0) + int(duration)
        time_spent[receiver] = time_spent.get(receiver, 0) + int(duration)

    return time_spent


def top_caller(time_spent_number):
    top_number = None
    top_duration = 0
    for number, duration in time_spent_number.items():
        if duration > top_duration:
            top_duration = duration
            top_number = number
    return top_duration, top_number


if __name__ == '__main__':
    time_spent_number = time_spent_number(calls)
    top_duration, top_number = top_caller(time_spent_number)

    print(f"{top_number} spent the longest time, {top_duration} seconds, on the phone during "
          f"September 2016.")

# 2O(N)






