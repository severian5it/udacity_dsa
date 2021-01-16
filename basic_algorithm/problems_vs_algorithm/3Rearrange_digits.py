import copy

def perm_rec(output, input):
    if not input:
        return output, input
    elif output == [[]]:
        a = input.pop()
        return perm_rec([[a]], input)
    else:
        l = len(output)
        a = input.pop()
        new_output = []
        for i in range(l+1):
            for j in output:
                new_list = copy.deepcopy(j)
                new_list.insert(i, a)
                new_output.append(new_list)
        return perm_rec(new_output, input)


def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    out, _ = perm_rec([[]], inputList)
    return out


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    break_idx = len(input_list)//2
    output = permute(input_list)
    max, max_array = 0, [0, 0]

    for o in output:
        a = int("".join(map(str, o[:break_idx])))
        b = int("".join(map(str, o[break_idx:])))
        c = a + b
        if c >= max:
            max = c
            max_array = [b, a]

    return max_array


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

