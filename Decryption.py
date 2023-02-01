def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char==" ":
            plaintext+=" "
        elif(char.isupper()):
            plaintext+=chr(((ord(char)-shift)-65)%26 + 65)
        else:
            plaintext+=chr(((ord(char)-shift)-97)%26 + 97)
    return plaintext

ciphertext = input("Enter Your Message to Decrypt: ")
shift = 1
print(caesar_decrypt(ciphertext, shift))