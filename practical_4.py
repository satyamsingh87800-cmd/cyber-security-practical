def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text):
            if text[i] == text[i+1]:
                prepared += "X"
            else:
                prepared += text[i+1]
                i += 1
        else:
            prepared += "X"
        i += 1
    return prepared

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    seen = set()
    
    for char in key + alphabet:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
            
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair_logic(text, key, mode):
    matrix = generate_matrix(key)
    text = prepare_text(text)
    result = ""
    shift = 1 if mode == 'encrypt' else -1

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])

        if r1 == r2: # Same row
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2: # Same column
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]
        else: # Rectangle swap
            result += matrix[r1][c2]
            result += matrix[r2][c1]
            
    return result

# User Interaction
msg = input("Enter message: ")
key = input("Enter keyword: ")

encrypted = playfair_logic(msg, key, 'encrypt')
decrypted = playfair_logic(encrypted, key, 'decrypt')

print(f"\nMatrix Key: {key.upper()}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted (Cleaned): {decrypted}")