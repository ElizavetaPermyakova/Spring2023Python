import typing as tp

en_abc = 'abcdefghijklmnopqrstuvwxyz'
en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    en_ABC_caesar = ''
    en_abc_caesar = ''
    ru_ABC_caesar = ''
    ru_abc_caesar = ''

    for i in range(len(en_ABC)):
        en_ABC_caesar += en_ABC[(i + shift) % len(en_ABC)]
    for i in range(len(en_abc)):
        en_abc_caesar += en_abc[(i + shift) % len(en_abc)]
    for i in range(len(ru_ABC)):
        ru_ABC_caesar += ru_ABC[(i + shift) % len(ru_ABC)]
    for i in range(len(ru_abc)):
        ru_abc_caesar += ru_abc[(i + shift) % len(ru_abc)]

    encrypt_en_ABC = str.maketrans(en_ABC, en_ABC_caesar)
    encrypt_en_abc = str.maketrans(en_abc, en_abc_caesar)
    encrypt_ru_ABC = str.maketrans(ru_ABC, ru_ABC_caesar)
    encrypt_ru_abc = str.maketrans(ru_abc, ru_abc_caesar)

    ciphertext = plaintext.translate(encrypt_en_ABC).translate(encrypt_en_abc).translate(encrypt_ru_ABC).translate(
        encrypt_ru_abc)

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
''