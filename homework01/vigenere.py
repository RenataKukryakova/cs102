def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for l in range(len(plaintext)):
        keyword = keyword.upper()
        pos = l % len(keyword)
        alph = ord(keyword[pos])-ord('A')
        if plaintext[l] == "":
            ciphertext += ""
            continue
        if plaintext[l].isupper():
            ciphertext = ciphertext+chr(ord('A')) + ((ord(plaintext[l]) - ord('A') + alph) % 26)
        elif "a" <= plaintext[l] <= "z":
            ciphertext = ciphertext+chr(ord('a')+((ord(plaintext[l])-ord('a')+alph) % 26))
        return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    zero = 0
    for l in range(len(ciphertext)):
        pos = (l-zero) % len(keyword)
        shift = ord(keyword[pos])-ord('A')
        if ciphertext[l] == "":
            plaintext += ""
            zero += 1
            continue
        if ciphertext.isupper():
            plaintext += chr(ord('A')+(ord(ciphertext[l]-ord('A')-shift) % 26))
        else:
            plaintext += chr(ord('a')+(ord(ciphertext[l])-ord(('a')-shift) % 26))

    return plaintext
