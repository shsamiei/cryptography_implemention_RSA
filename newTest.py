import random


def primes_inRange(x, y):
    prime_list = []
    for n in range(x, y):
        is_prime = True

        for num in range(2, n):
            if n % num == 0:
                is_prime = False

        if is_prime:
            prime_list.append(n)
    return prime_list


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(a, m):

    for x in range(1, m):
        if (a % m)*(x % m) % m == 1:
            return x
    raise Exception('The modular inverse does not exist.')


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair():
    prime_list = primes_inRange(100, 250)
    p = random.choice(prime_list)
    prime_list = primes_inRange(250, 350)
    q = random.choice(prime_list)
    print(p, q)

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    print(d)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    print(key)
    print(n)
    cipher = [pow(ord(char), key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((pow(char, key)) % n) for char in ciphertext]
    return ''.join(plain)


public, private = generate_keypair()

print("your public key is : ", public)
print("your private key is : ", private)

message = input('Enter your plain text : ')
encrypted_msg = encrypt(private, message)
print(''.join(map(lambda x: str(x), encrypted_msg)))

print(decrypt(public, encrypted_msg))
