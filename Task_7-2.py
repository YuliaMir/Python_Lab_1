'''Шифр Цезаря'''


s = str(input())
n = int(input())
def secret(s, n):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + n) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + n) % 26 + 97)
            encrypted_string += shifted_char
        else:
            encrypted_string += char
    return encrypted_string

print(secret(s, n))