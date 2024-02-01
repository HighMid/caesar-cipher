from caesar_cipher.corpus_loader import word_list, name_list
import re

def encrypt(plain, shifted):
    
    alphabet = 26
    start = 0
    encrypted_text = ""
    
    for char in plain:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            
            start_here = ord(char) - start
            shifted_start = (start_here + shifted) % alphabet
            encrypted_char = chr(shifted_start + start)
        else:
            encrypted_char = char
            
        encrypted_text += encrypted_char
        
    print(encrypted_text)
    return encrypted_text



def decrypt(encrypted, shifted):
    return encrypt(encrypted, -shifted)

def crack(encrypted):
    for shift in range(26):
        decrypted = encrypt(encrypted, -shift)
        words = decrypted.split()

        # Remove punctuation using regular expressions
        clean_words = [re.sub(r'[^\w\s]', '', word) for word in words]

        # Check if all words are legitimate
        if all(word.lower() in word_list or word in name_list for word in clean_words):
            return decrypted

    return ""
