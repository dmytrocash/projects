# Given an array of integers as strings and numbers, 
# return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    newlist = []
    for num in arr:
        newlist.append(int(num))
    return sum(newlist)

# alternative solutions:

# def sum_mix(arr):
#     return sum(map(int, arr))


# def sum_mix(arr):
#     return sum(int(n) for n in arr)