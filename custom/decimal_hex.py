# Convert a decimal to a hex

'''
For this challenge, you need to write a function in Python that accepts a string of ASCII characters. 
It should return each character's value as a hexadecimal string. Separate each byte by a space, and return all alpha hexadecimal characters as lowercase.

'''

def decimal_hex(text):

    list_asc_chars = list(text.lower())
    result_hexa = ''
    result_char = ''
    for c in list_asc_chars:
        result_hexa += hex(ord(c)) + ' '
        result_char += c + ' '
    return result_hexa + '\n' + result_char

print(decimal_hex("Ricardo"))



