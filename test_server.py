
import time, socket, sys
from newTest import primes_inRange, is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt
publicB, privateB = generate_keypair()
i = 0
t = 0
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
while True:
    conn, addr = s.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")

    s_name = conn.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
    conn.send(name.encode())

    while True:
        # first time just send my publicB :
        if i == 0:
            print("*****")
            print(publicB[0])
            print("*****")
            print(str(publicB[0]))
            print("*****")
            message = str(publicB[0])
            print("*****")
            print(message)
            print("*****")
            print(message.encode())
            print("*****")
            s.send(message.encode())
            i = 1

        else:
            message = input(str("Me : "))
            # Enc
            # if message == "[e]":
            #     message = "Left chat room!"
            #     conn.send(message.encode())
            #     print("\n")
            #     break
            message = encrypt(publicA, message)
            conn.send(message.encode())

        # -----------------------------------------------------------
        # recv :
        if t == 0:
            message = conn.recv(1024)
            message = message.decode()
            publicA = int(message)
            t = 1
        else:
            message = conn.recv(1024)
            message = message.decode()
            message = decrypt(privateB, message)
            print(s_name, ":", message)
