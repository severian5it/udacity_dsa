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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extract_code(number):
    """extract area code from number.
    Args:
        number: number to analyze
    Returns:
        area code
    """
    if number[0] == '(':
        first_bracket = number.find('(') + 1
        second_bracket =  number.find(')')
        return number[first_bracket:second_bracket]
    elif number[0:3] != '140':
        return number[0:4]
    else:
        return 140


def area_called(calls):
    """extract a set of area code from list of calls
    Args:
        calls: list of calls
    Returns:
        set of area codes
    """
    area_code = set()
    for call in calls:
        caller = call[0]
        receiver = call[1]
        if caller[0:5] == '(080)':
            prefix = extract_code(receiver)
            area_code.add(prefix)

    return area_code


def calls_by_area_code(calls):
    """extract a set of area code from list of calls
    Args:
        calls: list of calls
    Returns:
        area_code_calls: dictionary with area code as key and duration as value.
        total_calls: total number of calls from Bangalore Area.
    """
    area_code_calls = {}
    total_calls = 0
    for call in calls:
        caller = call[0]
        receiver = call[1]
        if caller[0:5] == '(080)':
            prefix = extract_code(receiver)
            area_code_calls[prefix] = area_code_calls.get(prefix, 0) + 1
            total_calls += 1

    return area_code_calls, total_calls


if __name__ == '__main__':
    print("The numbers called by people in Bangalore have codes:")
    area_calls = area_called(calls)
    sorted_bangalore_calls = sorted(area_calls)
    for code in sorted_bangalore_calls:
        print(code)

    area_code_calls, totals_calls = calls_by_area_code(calls)
    print(f"\n{(float(area_code_calls['080'])/float(totals_calls))*100:.2f} percent of calls from fixed lines "
          f"in Bangalore are calls "
          f"to other fixed lines in Bangalore.")
