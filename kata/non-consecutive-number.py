# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive 
# but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers. 
# The numbers will also all be unique and in ascending order. The numbers could be positive
#  or negative and the first non-consecutive could be either too!

def first_non_consecutive(arr):
    check_arr = list(range(arr[0], arr[-1]+1))
    newlist = []
    for x,y in zip(arr, check_arr):
        if x != y:
            newlist.append(x)
            return newlist[0]

# alternative solutions:

# def first_non_consecutive(arr):
#     if not arr: return 0
#     for i, x in enumerate(arr[:-1]):
#         if x + 1 != arr[i + 1]:
#             return arr[i + 1]


# def first_non_consecutive(arr):
#     for i in range(1, len(arr)):
#         if arr[i] - arr[i-1] > 1:
#             return arr[i]



