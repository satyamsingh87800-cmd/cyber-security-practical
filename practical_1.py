def encrypt(text, shift):
    result = ""
    shift = (shift % 26 + 26) % 26

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, 26 - (shift % 26))

message = input("Enter your message: ")
shift_value = int(input("Enter shift number: "))

encrypted_msg = encrypt(message, shift_value)
decrypted_msg = decrypt(encrypted_msg, shift_value)

print("\n--- Results ---")
print(f"Encrypted: {encrypted_msg}")
print(f"Decrypted: {decrypted_msg}")