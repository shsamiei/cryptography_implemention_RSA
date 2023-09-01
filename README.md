# Cryptographic Oracle

This project implements a simple cryptographic oracle using the RSA algorithm. It serves as a hands-on prototype to understand the role of oracles and gain experience with public-key cryptography.

## Overview

  Implements RSA key generation to create public and private key pairs. Keys are saved to files.
    Provides encryption and decryption functions using the generated RSA keys.
    Built a basic oracle interface with endpoints to encrypt user data and decrypt responses.
    User data is encrypted with the oracle's public key before sending to the oracle.
    The oracle decrypts requests with its private key and returns encrypted responses.
    Responses can only be decrypted by the user with their public key.

## Functionality

  Key generation - creates RSA key pairs and saves to PEM files
    Encryption - encrypts plaintext data with a RSA public key
    Decryption - decrypts ciphertext with private key
    Oracle server - basic HTTP interface to post encrypted requests
    Handles user request encryption before sending to oracle
    Decrypts oracle responses for the user

## Learnings

  Gained understanding of public-key cryptography and experience using RSA for encryption/decryption
    Learned how cryptographic oracles work at a basic level
    Implemented foundational oracle concepts like request encryption and response decryption
    Practiced secure key handling by saving keys to files instead of code
    Prototyped a simple interaction between a user and oracle server, This oracle implementation provides hands-on experience with core encryption concepts. The project can be extended to build production-grade oracle systems robust enough for blockchain platforms.
