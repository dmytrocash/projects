def list_of_strings(input_str):
    """This function accepts string with integers and symbols and make a list
    of strings with no spaces out of it.

    >>> list_of_strings('1+ 22-*/   333+ - 3239 - 23 + 2 - 1 +')
    ['1', '+', '22', '-', '*', '/', '333', '+', '-', '3239', '-', '23', '+', '2', '-', '1', '+']

    >>> list_of_strings('3 + 448 - 2 *        4/3')
    ['3', '+', '448', '-', '2', '*', '4', '/', '3']
    """
    modified_string = input_str.replace(' ', '')
    result = []
    num = ''
    for char in modified_string:
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

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
