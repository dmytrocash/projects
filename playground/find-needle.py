# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
# should return "found the needle at position 5" (in COBOL "found the needle at position 6")

def find_needle(haystack):
    index = haystack.index("needle")
    for n in haystack:
            if n == "needle":
                return f"found the {n} at position {index}"

# alternative solutions:

# def find_needle(haystack):
#     return 'found the needle at position {}'.format(haystack.index('needle'))