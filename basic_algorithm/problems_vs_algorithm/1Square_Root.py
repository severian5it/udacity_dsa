def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return 'Please provide a number'

    if number < 0:
        return 'Please provide a number greater than 0'

    if number in (0, 1):
        return number

    numbers = [i for i in range(1, number//2)]
    idx = number // 4

    while (numbers[idx] * numbers[idx]) > number:
        idx //= 2

    while (numbers[idx] * numbers[idx]) < number:
        idx += 1

    if (numbers[idx] * numbers[idx]) == number:
        return numbers[idx]
    else:
        return numbers[idx - 1]


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if(4 == sqrt(16)) else "Fail")
print("Pass" if(1 == sqrt(1)) else "Fail")
print("Pass" if(5 == sqrt(27)) else "Fail")

# Edge and corner cases
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if ('Please provide a number' == sqrt(None)) else "Fail")
print("Pass" if ('Please provide a number greater than 0' == sqrt(-200)) else "Fail")
print("Pass" if (1000 == sqrt(1000000)) else "Fail")



