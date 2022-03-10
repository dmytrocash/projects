# Given an array of integers.
# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
  
    if arr == [] : return []
    
    result = [0, 0]
    
    for value in arr:
        if value > 0:
            result[0] += 1
        else:
            result[1] += value
        
    return result

# alternative solutions:

# def count_positives_sum_negatives(arr):
#     return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []