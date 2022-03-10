# Given a string of digits, you should replace any digit below 5 with '0' 
# and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

def fake_bin(x):
    y = list(x)
    li = []
    for i in y:
        li.append(int(i))
    newlist = []
    for i in li:
        if i < 5:
            i = 0
            newlist.append(i)
        elif i >= 5:
            i = 1
            newlist.append(i)
    return "".join(map(str, newlist))


# alternative solutions:

# def fake_bin(x):
#     return ''.join(['0' if int(i) < 5 else '1' for i in x])