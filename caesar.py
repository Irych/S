def encrypt_caesar(plaintext):
    text = str(plaintext) 
    ciphertext = int(input()) 
    alph = 26  
    ind = 3 
    for i in range(len(text)): 
        char = text[i]
        if (65 <= ord(char)+ind <= 90) or (97 <= ord(char)+ind <= 122): 
            ciphertext += chr(ord(char)+ind) 
        else: 
            ciphertext += chr(ord(char)-alph+ind) 
    return ciphertext 


def decrypt_caesar(ciphertext): 
    text = str(ciphertext) 
    plaintext = int(input())
    alph = 26 
    ind = 3 
    for i in range(len(text)): 
        char = text[i] 
        if (65 <= ord(char)-ind <= 90) or (97 <= ord(text[i])-ind <= 122): 
            plaintext += chr(ord(char)-ind) 
    else: 
        plaintext += chr(ord(char)+alph-ind) 
    return plaintext
