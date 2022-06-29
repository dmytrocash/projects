# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

def correct(s):
    t = s.replace('1', 'I')
    u = t.replace('5', 'S')
    v = u.replace('0', 'O')
    return v

# alternative solutions:

# def correct(string):
#     return string.replace('1','I').replace('0','O').replace('5','S')


# def correct(string):
#     return string.translate(str.maketrans("501", "SOI"))


# def correct(string):
#   cor=''
#   for leter in string:
#     if leter =='1':
#       cor+='I'
#     elif leter=='5':
#       cor+='S'
#     elif leter=='0':
#       cor+='O'
#     else:
#       cor+=leter
#   return cor