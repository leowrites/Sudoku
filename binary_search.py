# binary tree search
import random
def binary_serch(input_array, value)->int:
    high = len(input_array) - 1
    low = 0
    half = int((high-low)/2) + low

    if input_array[low] == value:
        return low
    elif input_array[high] == value:
        return high
    elif input_array[half] == value:
        return half
    elif value > input_array[high] or value < input_array[low]:
        return -1

    while input_array[half] != value:
        if input_array[half] > value:
            high = half
            half = int((high-low)/2)
        elif input_array[half] < value:
            low = half
            half = int((high-low)/2) + low
        if high - low == 1:
            return -1

    if input_array[half] == value:
        return half

    return -1

test = sorted(list(set([random.randint(0, 1000) for x in range(0, 100)])))
x=39
print(test[x])
print(binary_serch(test, test[x]))