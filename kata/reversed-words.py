# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    list = s.split()[::-1]
    return " ".join(list)

# alternative solutions:

# def reverseWords(string):
#     return ' '.join(reversed(string.split()))


# def reverseWords(str):
#     str = str.split()
#     str = reversed(str)
#     return " ".join(str)


# def reverseWords(str):
#     return " ".join(str.split(" ")[::-1])