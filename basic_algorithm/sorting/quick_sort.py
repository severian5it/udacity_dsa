# complexity equals to O(nlogn) added some print to understand how pivot is moving around.
def sort_a_little_bit(items, begin_index, end_index):
    print(
        f'called sort a little bit on items: {items} between {items[begin_index]} and {items[end_index]}')
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):
        print(f'items: {items}, pivot: {items[pivot_index]}, processing now: {items[left_index]}')
        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    print(f'sort a little bit returning: {items}, with pivot: {items[pivot_index]}')
    return pivot_index


items = [8, 3, 1, 7, 0, 10, 2]
pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
print(items)
print('pivot index %d' % pivot_index)


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    # please note sorting is in place! So less space complexity.
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)


items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)

items = [1, 0]
quicksort(items)
print(items)

items = [96, 97, 98]
quicksort(items)
print(items)