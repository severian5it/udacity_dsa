'''
You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

prices = [3, 4, 7, 8, 6]

Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.

In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.
'''
import math

#my solution, i don't need indices, therefore no need of indices variable
def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    current_min_price, max_profit = math.inf, 0
    for price in prices:
        if price < current_min_price:
            current_min_price = price

        if price - current_min_price > max_profit:
            max_profit = price - current_min_price

    return max_profit


# udacity solution, is the same but it uses more variable, less readable
def max_returns(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0

    if len(arr) < 2:
        return

    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index

        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index

    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit

# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)