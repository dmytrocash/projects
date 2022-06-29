# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    if n == 0:
        return ""
    else:
        list1 = list(range(1, n+1))
        list2 = []
        for i in list1:
            list2.append(str(i))
        return " sheep...".join(list2) + ' sheep...'

# alternative solutions:

# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))


# def count_sheep(n):
#     sheep=""
#     for i in range(1, n+1):
#         sheep+=str(i) + " sheep..."
#     return sheep


# def count_sheep(n):
#     return ''.join(f'{x+1} sheep...' for x in range(n))