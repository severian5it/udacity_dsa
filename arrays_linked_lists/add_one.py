'''
You are given a non-negative number in the form of list elements.
For example, the number 123 would be provided as arr = [1, 2, 3].
Add one to the number and return the output in the form of a new list.
'''

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    num = int(''.join([str(a) for a in arr]))
    num +=1
    result = [int(t) for t in str(num)]
    return result

# alternate
def add_one(arr):
    borrow = 1;  # initial value

    """ 
    The three arguments of range() function are: 
    starting index, ending index(non-inclusive), and the increment/decrement value
    """
    # Traverse in reverse direction starting from the end of the list
    # The argument of range() functions are:
    # starting index, ending index (non exclusive), and the increment/decrement size
    for i in range(len(arr), 0, -1):

        # The "digit" denotes the updated Unit, Tens, and then Hunderd  position iteratively
        digit = borrow + arr[i - 1]

        '''
        The "borrow" will be carried to the next left digit 
        If the digit is between 0-9, borrrow will be 0. 
        If digit is 10, then the borrow will be 1.
        '''
        # The "//" is a floor division operator
        borrow = digit // 10

        if borrow == 0:
            # Update the arr[i - 1] with the updated digit, and quit the FOR loop.
            arr[i - 1] = digit
            break
        else:
            # Update the arr[i - 1] with the remainder of (digit % 10)
            arr[i - 1] = digit % 10

    # Prepend the final "borrow" to the original array.
    arr = [borrow] + arr

    # In this final updated arr, find a position (starting index) from where to return the list.
    # For [0, 1, 2, 4] , the position (starting index) will be 1
    # For [1, 0, 0, 0] , the position (starting index) will be 0
    position = 0
    while arr[position] == 0:
        position += 1

    return arr[position:]


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
