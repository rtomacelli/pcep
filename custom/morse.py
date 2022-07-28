# Using a dictionary to parse a common text to morse code
# This code convert a common text to morse code.

dict_morse = dict({'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.',  'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.-- ', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', ',' : '--..--', '?' : '..--..', '\'': '.----.', '!' : '-.-.--', '/' : '-..-.', '(' : '-.--.', ')' : '-.--.-', '&' : '.-...', ':' : '---...', ';' : '-.-.-.', '=' : '-...-', '+' : '.-.-.', '-' : '-....-', '_' : '..--.-', '\"': '.-..-.', '$' : '...-..-', '@' : '.--.-.', '¿' : '..-.-', '¡' : '--...-'})

def morse_parser(text):
    word = list(text.lower())
    morse_code = ''
    for i in range(0, len(word)):
        morse_code +=  ' ' if word[i] == ' ' else dict_morse.get(word[i]) + ' '
    print(morse_code)

morse_parser(input("Digite a mensagem a ser enviada: "))