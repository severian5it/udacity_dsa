def binary_search_recursive_soln(array, target, start_index, end_index):
    ''' recursive search taking into account of the rotation
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: start index of the portion of the array you search
      end_index: end index of the portion of the array you search
    returns:
      int: the index of the target, if found, in the source
       -1: if the target is not found
    '''
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]
    first_element = array[start_index]
    last_element = array[end_index]

    if mid_element == target:
        return mid_index
    elif first_element == target:
        return start_index
    elif last_element == target:
        return end_index
    elif mid_element > target > first_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    elif mid_element < target < last_element:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
    elif mid_element < target > last_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    elif mid_element > target < last_element:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


def binary_search_recursive(array, target):
    ''' facing function for binary search
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return 'empty array'

    if number is None:
        return 'please specify Target'

    return binary_search_recursive(input_list, number)


def linear_search(input_list, number):
    '''  linear search in O(n) time, used for testing
    args:
      input_list: a sorted array of items of the same type
      number: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if len(input_list) == 0:
        return 'empty array'

    if number is None:
        return 'please specify Target'
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print(linear_search(input_list, number), rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge and corner cases
test_function([[6, 7, 8, 1, 2, 3, 4], None])
test_function([[], 10])