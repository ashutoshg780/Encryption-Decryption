def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char==" ":
            ciphertext+=" "
        elif(char.isupper()):
            ciphertext+=chr(((ord(char)+shift)-65)%26 + 65)
        else:
            ciphertext+=chr(((ord(char)+shift)-97)%26 + 97)
    return ciphertext

plaintext = input("Enter Your Message to Encrypt: ")
shift=1
print(encrypt_caesar(plaintext, shift))