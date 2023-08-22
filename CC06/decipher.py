with open("message.txt", 'r') as ifh:
    text = [i.strip() for i in ifh.readlines()]

text = ''.join(text)


def simple_substitution_decrypt(text, key):
    """Decrypts a simple substitution cipher using a given key."""
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted_text += char
    return decrypted_text


for i in range(-27, 27):
    print(f"KEY : {i}")
    decrypted_text_key_x = simple_substitution_decrypt(text, i)
    print(decrypted_text_key_x[-65:])
    print("--------")
