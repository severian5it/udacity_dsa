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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count_distinct_occurence(calls, texts):
    """Return the count of distinct occurence of number
    Args:
        calls: list of calls
        texts: list of texts
    Returns:
        number of distinct number
    """
    number_set = set()
    for record in calls+texts:
        number_set.add(record[0])
        number_set.add(record[1])

    return len(number_set)


if __name__ == '__main__':
    nbr_telephones = count_distinct_occurence(calls, texts)
    print(f"There are {nbr_telephones} different telephone numbers in the records")





