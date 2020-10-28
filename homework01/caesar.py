import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
alpha=list(plaintext)
for letter in alpha:
    letter=ord(letter)
    if (letter > ord('A') and letter <= ord('Z') or (letter >= ord('a')) and letter <= ord('z') ):
    if (letter > ord('Z') - shift) and (letter <= ord('Z')):
         letter -=26
    elif (letter > (ord('z') - shift)) and (letter <= ord('z')):
        letter-= 26
         letter += shift
         letter = chr(letter)
         ciphertext = ciphertext + letter
return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alpha= list(plaintext)
    for letter in alpha:
        letter=ord(letter)
        if (letter >= ord('A') and letter <= ord('Z')) or (letter >= ord('a') and letter <= ord ('z')):
            if (letter >= ord('A') and letter < (ord('A') + shift)):
                letter += 26
            elif (letter >= ord('a') and letter <= (ord('a') + shift)):
                letter += 26
                letter -= shift
                letter = chr(letter)
                plaintext=plaintext + letter
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for key in range (len(letters)):
        translated=''
        for symbol in message:
            if symbol in letters:
                num=letters.find(symbol)
                num=num-key
                if num<0:
                    num=num+len(letters)
                    translated=translated+symbol


    return best_shift
