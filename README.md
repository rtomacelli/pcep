# 10 Python code challenges

## Create a Morse code translator
We no longer use Morse code to transfer information, but that doesn't mean you can't use it in a code challenge. Write a function in Python that takes in a string that can have alphanumeric characters in lower or upper case.
The string can also contain any special characters handled in Morse code, including commas, colons, apostrophes, periods, exclamation marks, and question marks. The function should return the Morse code equivalent for the string.

## Write a Friday 13th detector
Create a function in Python that accepts two parameters. They’ll both be numbers. The first will be the month as a number, and the second will be the four-digit year. The function should parse the parameters and return True if the month contains a Friday the 13th and False if it doesn’t.

## Find the domain name using an IP address
For this Python challenge, you'll want to import the Python socket library. That’s the only hint. Write a function that accepts an IP address, makes a DNS request, and returns the domain name that maps to that IP address using PTR DNS records.

## Parse an encoded string
In this Python challenge, you need to write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.

Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.

An example input would be "Robert000Smith000123". The function should return the following using that input:

{ "first_name": "Robert", "last_name": "Smith", "id": "123" }

## Convert a decimal to a hex
For this challenge, you need to write a function in Python that accepts a string of ASCII characters. It should return each character's value as a hexadecimal string. Separate each byte by a space, and return all alpha hexadecimal characters as lowercase.

## Find the difference between the strings
Write a function in Python that accepts two string parameters. The first parameter will be a string of characters, and the second parameter will be the same string of characters, but they’ll be in a different order and have one extra character. The function should return that extra character.

For example, if the first parameter is "eueiieo" and the second is "iieoedue," then the function should return "d."

## Shadow sentences
For the purpose of this challenge, shadow sentences are sentences where every word is the same length and order but without any of the same letters. Write a function that accepts two parameters that may or may not be shadows of each other. The function should return True if they are and False if they aren’t.

An example would be "they are round" and "fold two times," which are shadow sentences, while "his friends" and "our company" are not because both contain an r.

## Tic Tac Toe blocker
In this Python challenge, write a function that’ll accept two numbers. These numbers will represent a position on a tic-tac-toe board. They can be 0 through 8, where 0 is the top-left spot, and 8 is the bottom-right spot.

These parameters are two marks on the tic-tac-toe board. The function should return the number of the spot that can block these two spots from winning the game.

## Rearrange the number
To complete this challenge, write a function that accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.

For example, if the parameter is "213", the function should return "198", which is the result of 123 subtracted from 321.

## Duplicate letter checker
Create a function in Python that accepts one parameter: a string that’s a sentence. This function should return True if any word in that sentence contains duplicate letters and False if not.

By [code academy](https://www.codecademy.com/resources/blog/advanced-python-code-challenges/)


https://www.fullstack.cafe/blog/big-o-interview-questions
