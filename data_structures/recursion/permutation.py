import copy

## my solution below, but it needs 2 parameters
def perm_list(output, input):
    if not input:
        return output, input
    elif output == [[]]:
        a = input.pop()
        return perm_list([[a]], input)
    else:
        l = len(output)
        a = input.pop()
        new_output = []
        for i in range(l+1):
            for j in output:
                new_list = copy.deepcopy(j)
                new_list.insert(i, a)
                new_output.append(new_list)
        return perm_list(new_output, input)


def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    out, _ = perm_list([[]], inputList)
    return out

### udacity solution I don't think is easier to read.
import copy  # We will use `deepcopy()` function from the `copy` module


def permute(inputList):
    # a compound list
    finalCompoundList = []  # compoundList to be returned

    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])

    else:
        first_element = inputList[0]  # Pick one element to be permuted
        after_first = slice(1, None)  # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list

        # Recursive function call
        sub_compoundList = permute(rest_list)

        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:

            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1):
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)

                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)

                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)

    return finalCompoundList


# Test Cases

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]),
                              [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1],
                               [2, 1, 0]])) else "Fail")