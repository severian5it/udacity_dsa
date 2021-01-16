def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list or len(input_list) == 1:
        return "please specify a list of more than 1 element"
    list_sorted = mergesort(input_list)
    a, b = [], []
    for idx, i in enumerate(list_sorted[::-1]):
        if idx%2 == 0:
            a.append(i)
        else:
            b.append(i)

    a = int("".join(map(str, a)))
    b = int("".join(map(str, b)))

    print(a, b)
    return [a, b]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[2, 1, 9, 7, 8], [971, 82]])
test_function([[1, 3], [3, 1]])


print(rearrange_digits(None))
print(rearrange_digits([]))
print(rearrange_digits([1]))






