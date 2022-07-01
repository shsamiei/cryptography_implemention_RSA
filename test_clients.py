import time, socket, sys
from newTest import primes_inRange, is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

# client.py ,  we suppose it as Alice

# first of all generate pk and sk for Alice

publicA, privateA = generate_keypair()

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")
i = 0
t = 0
while True:
    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

    while True:
        if t == 0:
            message = s.recv(1024)
            message = message.decode()
            print("----")
            print(message)
            print("----")
            # print(type(message))
            # print(int(message))
            publicB = int(message)
            t = 1

        else:
            message = s.recv(1024)
            message = message.decode()
            message = decrypt(privateA, message)
            print(s_name, ":", message)

# ------------------------------------------------------------
        # first time just exchange public key and secure key :
        if i == 0:
            message = str(publicA[0])
            s.send(message.encode())
            i = 1
        else:
            message = input(str("Me : "))
            encrypted_msg = encrypt(publicB, message)
            encrypted_msg = ''.join(map(lambda x: str(x), encrypted_msg))
            s.send(encrypted_msg.encode())



