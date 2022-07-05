alpha ="abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift =3):
    encrypted_str=""
    for c in s:
        index =alpha.index(c)
        shifted_index = (index + shift) % len(alpha)
        encrypted_str += alpha[shifted_index]
    return encrypted_str

print(encrypt("helloworld"))