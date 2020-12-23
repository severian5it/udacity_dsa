# my solution, using is instance
def deep_reverse(arr):
    output = []
    for a in arr[::-1]:
        if isinstance(a,list):
            output.append(deep_reverse(a))
        else:
            output.append(a)
    return output


# Recursive Solution, udacity, pretty much the same

def deep_reverse(arr):
    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = []  # final list to be returned

    '''Traverse the given list (array) in the reverse direction using extended slice.'''
    # For a given list, sample syntax are - myList[1:10:2], myList[:-1:1], myList[::-1]
    # The first argument is the starting index of the slice (inclusive),
    # second argument is the ending index of the slice (exclusive),
    # third argument is the increment/decrement step size.
    # If we do not specify an argument, it means to consider all elements from that end of the list.
    for item in arr[::-1]:

        # If this item is a list itself, invoke deep_reverse to reverse the items recursively.
        if type(item) is list:
            item = deep_reverse(item)

        # append the item to the final list
        reversed_items.append(item)

    return reversed_items


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)