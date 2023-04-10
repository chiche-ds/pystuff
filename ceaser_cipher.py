alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ")
text = input("Type your message: ").lower()
shift = int(input("type the shif number"))

def encrypt(text=text, shift=shift ):
    word = ""
    for latter in text:
        test = alphabet.index(latter)
        result = alphabet[test+shift]
        word += result
    print(word)

def decrypt(text=text, shift=shift ):
    word = ""
    for latter in text:
        test = alphabet.index(latter)
        result = alphabet[test-shift]
        word += result
    print(word)


decrypt()