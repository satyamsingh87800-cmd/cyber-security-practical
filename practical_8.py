def power(a, b, p):
    return pow(a, b, p)

def main():
    P = int(input("Enter a prime number (P): "))
    G = int(input("Enter a primitive root for P (G): "))

    a = int(input("Alice: Enter your private key: "))
    x = power(G, a, P)
    print(f"Alice's public value sent to Bob (x): {x}")

    b = int(input("Bob: Enter your private key: "))
    y = power(G, b, P)
    print(f"Bob's public value sent to Alice (y): {y}")

    ka = power(y, a, P)
    kb = power(x, b, P)

    print(f"\nAlice's calculated shared secret: {ka}")
    print(f"Bob's calculated shared secret: {kb}")

    if ka == kb:
        print("Success: Shared secrets match!")
    else:
        print("Error: Shared secrets do not match.")

if __name__ == "__main__":
    main()