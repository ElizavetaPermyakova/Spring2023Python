def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypts plaintext using a Vigenere cipher."""
    ciphertext = ''
    keyword = keyword.lower()
    a = 0
    while len(keyword) < len(plaintext):
        keyword += keyword[a : a + 1]
        a += 1

    for i in range(len(plaintext)):
        limit = 122 #конец нижнего регистра
        if plaintext[i].isupper():
            limit = 90 #верхний регистр
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
        if ord(plaintext[i]) + ord(keyword[i]) % 97 <= limit:
            symbol = chr(ord(plaintext[i]) + ord(keyword[i]) % 97)
        else:
            symbol = chr((ord(plaintext[i]) + ord(keyword[i]) % 97) - 26)
        ciphertext += symbol
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypts a ciphertext using a Vigenere cipher."""
    plaintext = ''
    keyword = keyword.lower()
    a = 0
    while len(keyword) < len(ciphertext):
        keyword += keyword[a : a + 1]
        a += 1

    for i in range(len(ciphertext)):
        limit = 97 #начало нижнего регистра
        if ciphertext[i].isupper():
            limit = 65 #начало верхнего регистра
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
        if ord(ciphertext[i]) - ord(keyword[i]) % 97 >= limit:
            symbol = chr(ord(ciphertext[i]) - ord(keyword[i]) % 97)
        else:
            symbol = chr((ord(ciphertext[i]) - ord(keyword[i]) % 97) + 26)
        plaintext += symbol
    return plaintext
