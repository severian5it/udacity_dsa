import collections
from operator import attrgetter

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    max_per_weight = [0]*(knapsack_max_weight+1)

    for item in sorted(items, key=attrgetter('weight')):
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if capacity >= item.weight:
                max_per_weight[capacity] = max(max_per_weight[capacity - item.weight] + item.value, max_per_weight[capacity])

    return max_per_weight[-1]

tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])