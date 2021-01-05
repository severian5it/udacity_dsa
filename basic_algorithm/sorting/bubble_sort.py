# overall complexity is O(n^2), so n comparison for n steps.
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
        for iteration in range(len(l)):
            for index in range(1, len(l)):
                this = l[index]
                prev = l[index - 1]

                if (prev[0] > this[0]) or(prev[0] == this[0] and prev[1] >= this[1]):
                    continue

                l[index] = prev
                l[index - 1] = this

bubble_sort_2(sleep_times)
print(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")