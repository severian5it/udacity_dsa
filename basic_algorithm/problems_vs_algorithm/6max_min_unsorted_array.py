import random


def get_min_max(ints):
    '''  returning max and min in a integer list
    args:
      ints: an unsorted array of integers

    returns:
      (max, min): tuple containing max and min
    '''
    if not ints:
        return (None, None)

    min = ints[0]
    max = ints[0]
    for i in ints:
        if i <= min:
           min = i

        if i >= max:
            max = i

    return (min, max)


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [1,2,3]
print("Pass" if ((1, 3) == get_min_max(l)) else "Fail")

# edge cases

l = []
print(get_min_max(l)) # should return None, None
l = None
print(get_min_max(l)) # should return None, None
