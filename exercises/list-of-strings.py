a = "1+ 22-*/   333+ - 3239 - 23 + 2 - 1 +".replace(' ', '')

result = []
num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            result.append(num)
            num = ''
        if char.isnumeric() is False:
            result.append(char)
if num != '':
    result.append(num)
print(result)

# ['1', '+', '22', '-', '*', '/', '333', '+', '-', '3239', '-', '23', '+', '2', '-', '1', '+']
