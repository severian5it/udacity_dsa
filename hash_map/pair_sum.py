# mine, is shorter buy O(2N)
def pair_sum_to_target(input_list, target):
    # TODO: Write pair sum to target function
    cache_missing = {target - v: idx for idx, v in enumerate(input_list)}

    for idx, v in enumerate(input_list):
        missing_idx = cache_missing.get(v)
        if missing_idx:
            return [missing_idx, idx]

    return [-1, -1]

# udacity, more interesting, it creates dictionary on the way.
def pair_sum_to_target(input_list, target):
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    index_dict = dict()

    # Traverse through the input_list
    for index, element in enumerate(input_list):

        # `in` is the way to test for the existence of a "key" in a dictionary
        if (target - element) in index_dict:
            # Return the TWO indices that sum to the target
            return [index_dict[target - element], index]

        index_dict[element] = index

    return [-1, -1]  # If the target is not achieved


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)