import typing as tp

en_abc = 'abcdefghijklmnopqrstuvwxyz'
en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    eng_A_caesar = ''
    eng_a_caesar = ''
    rus_A_caesar = ''
    rus_a_caesar = ''

    for i in range(len(en_ABC)):
        eng_A_caesar += en_ABC[(i + shift) % len(en_ABC)]
    for i in range(len(en_abc)):
        eng_a_caesar += en_abc[(i + shift) % len(en_abc)]
    for i in range(len(ru_ABC)):
        rus_A_caesar += ru_ABC[(i + shift) % len(ru_ABC)]
    for i in range(len(ru_abc)):
        rus_a_caesar += ru_abc[(i + shift) % len(ru_abc)]

    encrypt_eng_A = str.maketrans(en_ABC, eng_A_caesar)
    encrypt_eng_a = str.maketrans(en_abc, eng_a_caesar)
    encrypt_rus_A = str.maketrans(ru_ABC, rus_A_caesar)
    encrypt_rus_a = str.maketrans(ru_abc, rus_a_caesar)

    ciphertext = plaintext.translate(encrypt_eng_A).translate(encrypt_eng_a).translate(encrypt_rus_A).translate(
        encrypt_rus_a)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:

    en = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    plaintext = ''
    for i in ciphertext:
        if i in en:
            for j in ciphertext:
                if j.isupper():
                    index = ord(j) - ord('A')
                    shift2 = (index - shift) % 26 + ord('A')
                    root = chr(shift2)
                    plaintext += root
                elif j.islower():
                    index = ord(j) - ord('a')
                    shift2 = (index - shift) % 26 + ord('a')
                    root = chr(shift2)
                    plaintext += root
                else:
                    plaintext += j
            break
        elif i in ru:
            for j in ciphertext:
                if j.isupper():
                    index = ord(j) - ord('А')
                    shift2 = (index - shift) % 33 + ord('А')
                    root = chr(shift2)
                    plaintext += root
                elif j.islower():
                    index = ord(j) - ord('а')
                    shift2 = (index - shift) % 33 + ord('а')
                    root = chr(shift2)
                    plaintext += root
                else:
                    plaintext += j
        break

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """ Brute force breaking a Caesar cipher."""
    best_shift = 0
    shift = ciphertext
    while shift not in dictionary:
        best_shift += 1
        shift = encrypt_caesar(ciphertext, best_shift)
    return best_shift
""