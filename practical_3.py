def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    cipher_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isalpha():
            # Calculate shift based on the key character
            base = ord('A') if char.isupper() else ord('a')
            key_base = ord('A') if key[i].isupper() else ord('a')
            
            shift = ord(key[i]) - key_base
            # Apply shift and wrap around alphabet
            x = (ord(char) - base + shift) % 26
            cipher_text.append(chr(x + base))
        else:
            cipher_text.append(char)
    return "".join(cipher_text)

def decrypt_vigenere(cipher_text, key):
    orig_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_base = ord('A') if key[i].isupper() else ord('a')
            
            shift = ord(key[i]) - key_base
            # Reverse the shift
            x = (ord(char) - base - shift) % 26
            orig_text.append(chr(x + base))
        else:
            orig_text.append(char)
    return "".join(orig_text)

# User Interaction
print("--- Polyalphabetic Cipher (Vigenère) ---")
text = input("Enter message: ")
keyword = input("Enter keyword (letters only): ")

if not keyword.isalpha():
    print("Error: Keyword must only contain letters.")
else:
    encrypted = encrypt_vigenere(text, keyword)
    decrypted = decrypt_vigenere(encrypted, keyword)

    print(f"\nEncrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")