from re import split

# Parse an encoded string
def decode_string(text):

    dict_user = { "first_name" : "", "last_name"  : "", "id": "" }
    valor     = split(r"[0]{3,}", text)

    for indice, chave in enumerate(dict_user):
        dict_user[chave] = valor[indice]

    print(dict_user)

decode_string("Robert000Smith000123")