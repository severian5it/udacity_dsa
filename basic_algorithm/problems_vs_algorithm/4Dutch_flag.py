def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return 'please provide input list'
    front_index = 0
    final_index = len(input_list) -1
    while front_index < final_index:
        if input_list[front_index] == 2:
            del input_list[front_index]
            input_list.append(2)
            final_index -= 1
        elif input_list[front_index] == 0:
            del input_list[front_index]
            input_list.insert(0, 0)
            front_index += 1
        else:
            front_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge case
print(sort_012(None))
print(sort_012([]))
print(sort_012([0])) #especting same as input
