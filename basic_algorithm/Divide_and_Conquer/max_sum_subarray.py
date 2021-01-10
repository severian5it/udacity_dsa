# this is the most efficient subarray sum in O(N), and is limit the space complexity
def maxCrossingSum(arr, start, mid_idx, stop):
    mid_idx_val = arr[mid_idx]
    len_arr = len(arr)
    leftMaxSum = 0
    rightMaxSum = 0
    for i in range(mid_idx, start - 1, -1):
        print('left', i)
        leftMaxSum += arr[i]

    for i in range(mid_idx + 1, stop+1):
        print('right', i)

        rightMaxSum += arr[i]

    print(f'mid is {mid_idx}, mid idx val is {mid_idx_val}, '
          f'len is {len_arr}, leftMaxSum is {leftMaxSum}, rightMaxSum is {rightMaxSum}')
    return leftMaxSum + rightMaxSum


def maxSubArrayRecursive(arr, start, stop):
    print(arr, start, stop)
    if start == stop:
        return arr[start]

    mid_idx = start + (stop - start -1)//2

    L = maxSubArrayRecursive(arr, start, mid_idx)
    R = maxSubArrayRecursive(arr, mid_idx + 1, stop)
    C = maxCrossingSum(arr, start, mid_idx, stop)
    max_reach = max(C, max(L, R))
    print(f'Maximum reached {max_reach}')
    return max_reach


def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.

    mid_idx = len(arr)//2
    mid_idx_val = arr[mid_idx]
    len_arr = len(arr)
    leftMaxSum = 0
    rightMaxSum = 0
    for i in range(mid_idx, -1, -1):
        print('left', i)
        leftMaxSum += arr[i]

    for i in range(mid_idx +1, len_arr):
        print('right', i)

        rightMaxSum += arr[i]

    print(f'mid is {mid_idx}, mid idx val is {mid_idx_val}, '
          f'len is {len_arr}, leftMaxSum is {leftMaxSum}, rightMaxSum is {rightMaxSum}')
    return leftMaxSum + rightMaxSum
    '''
    return maxSubArrayRecursive(arr, 0, len(arr)-1)


# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 6

# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 10

# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 7