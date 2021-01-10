def get_min_max(ints):
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

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")