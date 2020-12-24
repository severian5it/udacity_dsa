"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
MIN_STEPS = {0: 0, 1:1, 2:2, 3:4}


def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
    if n <=3:
        return MIN_STEPS[n]

    # Recursive Step - Split the solution into base case if n > 3.

    more_steps = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    return more_steps

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print(output, solution)
        print("Fail")

n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)