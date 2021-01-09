def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    l = len(Arr)
    groups = []
    list_to_app = []
    Medians = []
    for idx, i in enumerate(Arr):
        if (idx+1) % 6 == 0:
            list_to_app.sort()
            groups.append(list_to_app)
            Medians.append(list_to_app[len(list_to_app)//2])
            list_to_app = []
        else:
            list_to_app.append(i)
    if list_to_app:
        list_to_app.sort()
        groups.append(list_to_app)
        Medians.append(list_to_app[len(list_to_app) // 2])

    pivot = Medians[len(Medians)//2] # it suggest however 𝑓𝑎𝑠𝑡𝑆𝑒𝑙𝑒𝑐𝑡(𝑆,𝑛10)
    arr_less_p = [a for a in Arr if a < pivot]
    arr_eq_p = [a for a in Arr if a == pivot]
    arr_more_p = [a for a in Arr if a > pivot]

    print(f'these are the {groups}, these are the  {Medians}, this is the {pivot}, '
          f'these are the partitions: {arr_less_p}, {arr_eq_p}, {arr_more_p}')

    if k <= len(arr_less_p):
        return fastSelect(arr_less_p, k)
    elif k > len(arr_less_p) + len(arr_eq_p):
        return fastSelect(arr_more_p, (k - len(arr_less_p) - len(arr_eq_p)))
    else:
        return pivot



Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99