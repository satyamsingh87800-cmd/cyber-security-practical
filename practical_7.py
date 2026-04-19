import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
msg = int(input("Enter message (as a number): "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = mod_inverse(e, phi)

encrypted = pow(msg, e, n)
decrypted = pow(encrypted, d, n)

print(f"\nPublic Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")