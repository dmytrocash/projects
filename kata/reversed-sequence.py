# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]

def make_negative( number ):
    if number <= 0:
        pass
    else:
        number = number * (-1)
    return number

# alternative solutions:

# def make_negative( number ):
#     return -number if number>0 else number