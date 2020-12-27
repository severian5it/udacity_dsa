def get_code(int_to_traslate):
    return chr(ord('`') + int_to_traslate)

# mine not working
def all_codes_func(output,num_array):
    print('num_array', output, num_array)
    to_check = [int(n) > 26 for n in num_array]
    if any(to_check):
        print('out', output, num_array)
        return output, num_array
    else:
        print('else')
        output.append(num_array)
        l = len(num_array)
        new_array = []
        print('before loop', output)
        if l == 1:
            return output, num_array
        for i in range(l-1):
            j = i+1
            print('loop', i,j )
            [new_array.append(n) for n in num_array[:i]]
            new_array.append(num_array[i]+num_array[j])
            [new_array.append(n) for n in num_array[j+1:]]
            print('new_array', new_array)
            return all_codes_func(output, new_array)

# more similar to keypad, instead of doing permutation on list, it breaks the number digits
# from right to left
def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)


def all_codes(number):
    if number == 0:
        return [""]

    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9:

        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)

        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet

    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10

    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)

    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output

def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    num_array = [s for s in str(number)]

    codes, _ = all_codes_func([], num_array)
    print('exit', codes, _)
    return [get_code(int(''.join(c))) for c in codes]


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)

print(get_code(4))

print(get_code(1000))