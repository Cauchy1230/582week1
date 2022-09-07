def encrypt(key, plaintext):
    ciphertext = ""
    for c in plaintext:
        seq = (ord(c) - 65 + key) % 26
        n_c = str(seq + 65)
        ciphertext += n_c
    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        seq = (ord(c) - 65 - key) % 26
        n_c = str(seq + 65)
        plaintext += n_c
    return plaintext
