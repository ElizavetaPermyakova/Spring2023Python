def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypts plaintext using a Vigenere cipher."""
    keyword = keyword.lower()
    ciphertext = ''
    i = 0
    a = len(keyword)
    b = len(plaintext)

    while a < b:
        keyword += keyword[i: i + 1]
        i += 1

    for j in range(b):
        limit = 122  # последняя буква в нижнем регистре
        if plaintext[j].isupper():
            limit = 90  # последняя буква в верхнем регистре
        if not plaintext[j].isalpha():
            ciphertext += plaintext[j]
            continue
        if (ord(plaintext[j]) + ord(keyword[j]) % 97 <= limit):
            letter = chr(ord(plaintext[j]) + ord(keyword[j]) % 97)
        else:
            letter = chr((ord(plaintext[j]) + ord(keyword[j]) % 97) - 26)
        ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypts a ciphertext using a Vigenere cipher."""
    plaintext = ''
    keyword = keyword.lower()
    i = 0
    a = len(keyword)
    b = len(ciphertext)

    while a < b:
        keyword += keyword[i: i + 1]
        i += 1

    for j in range(b):
        limit = 97
        if ciphertext[j].isupper():
            limit = 65
        if not ciphertext[j].isalpha():
            plaintext += ciphertext[j]
            continue
        if (ord(ciphertext[j]) - ord(keyword[j]) % 97 >= limit):
            letter = chr(ord(ciphertext[j]) - ord(keyword[j]) % 97)
        else:
            letter = chr((ord(ciphertext[j]) - ord(keyword[j]) % 97) + 26)
        plaintext += letter
    return plaintext
