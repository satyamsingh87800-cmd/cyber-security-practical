import string

def monoalphabetic_cipher(text, key, mode='encrypt'):
    alphabet = string.ascii_lowercase
    key = key.lower()
    
    # Create a mapping dictionary
    if mode == 'encrypt':
        mapping = dict(zip(alphabet, key))
    else:
        mapping = dict(zip(key, alphabet))
    
    result = ""
    for char in text:
        if char.lower() in mapping:
            # Map the character and preserve the original case
            new_char = mapping[char.lower()]
            result += new_char.upper() if char.isupper() else new_char
        else:
            # Keep numbers and symbols as they are
            result += char
            
    return result

# User Interaction
print("--- Monoalphabetic Cipher ---")
message = input("Enter your message: ")

# A sample key (must be 26 unique letters)
# Example: 'qwertyuiopasdfghjklzxcvbnm'
key = input("Enter a 26-letter substitution key: ")

if len(set(key)) != 26 or not key.isalpha():
    print("Error: Key must contain exactly 26 unique alphabetic characters.")
else:
    encrypted = monoalphabetic_cipher(message, key, 'encrypt')
    decrypted = monoalphabetic_cipher(encrypted, key, 'decrypt')

    print(f"\nEncrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")