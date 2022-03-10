# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

import math
def century(year): 
    if year % 100 == 0:
        return math.trunc(year/100)
    else:
        return math.trunc(year/100+1)

# alternative solutions:

# def century(year):
#     return (year + 99) // 100


# import math
# def century(year):
#     return math.ceil(year / 100)