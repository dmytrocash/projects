# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    name1 = str.title(name)
    name2 = name1.split()
    l1 = name2[0][0]
    l2 = name2[1][0]
    result = l1 + "." + l2
    return result   

# alternative solutions:
# def abbrevName(name):
#     names = name.split()
#     return f"{names[0][0]}.{names[1][0]}".upper()


# def abbrevName(name):
#     return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()