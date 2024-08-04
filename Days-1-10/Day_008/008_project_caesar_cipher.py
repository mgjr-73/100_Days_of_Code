import caesarart

print(caesarart.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift):
    if direction == "encode":
        cipher_text = []
        for character in text:
            x = alphabet.index(character)
            y = (len(alphabet)-1)
            if x + shift > y:
                cipher_text += alphabet[(x + shift)-(y+1)]
            else:
                cipher_text += alphabet[x + shift]
        output = ''.join(cipher_text)
        print(f"The encoded text is: {output}")
    else:
        decrypted_text = []
        for character in text:
            x = alphabet.index(character)
            y = (len(alphabet)-1)
            if x + shift > y:
                decrypted_text += alphabet[(x - shift)+(y+1)]
            else:
                decrypted_text += alphabet[x - shift]
        output = ''.join(decrypted_text)
        print(f"The decrypted text is: {output}")

# Validate shift value so it doesn't go over index value of 25
if shift > 26:
    shift = shift % 26

caesar(text, shift)


