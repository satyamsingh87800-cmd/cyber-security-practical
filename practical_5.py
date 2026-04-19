import numpy as np

def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

def get_matrix_inverse(matrix, m):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = modInverse(det % m, m)
    if det_inv == -1:
        raise ValueError("Matrix not invertible")
    matrix_inv = np.linalg.inv(matrix) * det
    adjugate = np.round(matrix_inv).astype(int) % m
    return (det_inv * adjugate) % m

def hill_cipher(text, key_matrix, mode='encrypt'):
    text = text.upper().replace(" ", "")
    while len(text) % 3 != 0:
        text += 'X'
    res = ""
    if mode == 'decrypt':
        key_matrix = get_matrix_inverse(key_matrix, 26)
    for i in range(0, len(text), 3):
        block = [ord(c) - ord('A') for c in text[i:i+3]]
        transformed_block = np.dot(key_matrix, block) % 26
        res += "".join(chr(int(num) + ord('A')) for num in transformed_block)
    return res

key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
msg = input("Enter message: ")

try:
    encrypted = hill_cipher(msg, key, 'encrypt')
    decrypted = hill_cipher(encrypted, key, 'decrypt')
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
except ValueError as e:
    print(e)