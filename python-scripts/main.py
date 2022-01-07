
import sys
from getopt import GetoptError, getopt

argv = sys.argv[2:]

# print(argv)

first = sys.argv[1]

if first == 'encrypt':
    algorithm = ''
    message= ''
    key= ''

    opts, args = getopt(argv,'a:m:k:')
    
    data = dict(opts)
    # print(data['-a'] == "ceasar")
    if data['-a'] == 'ceasar':
        try:
            key = int(data['-k'])
        except Exception as e:
            print('Key has to be a number')
            exit()
        from ciphers.ceasar import CeasarCipher
        print(CeasarCipher.encrypt(data['-m'], key))
        sys.stdout.flush()

    elif data['-a'] == 'vigenere':
        from ciphers.vigenere import VigenereCipher
        print(VigenereCipher.encrypt(data['-m'],data['-k']))
        sys.stdout.flush()


    elif data['-a'] == 'substitution':
        from ciphers.substitution import SubstitutionCipher
        alphabets = data['-k'].split(' ')[::-1]
        print(SubstitutionCipher.encrypt(data['-m'],*alphabets))
        sys.stdout.flush()
    
    elif data['-a'] == 'transposition':
        try:
            key = int(data['-k'])
        except Exception as e:
            print('Key has to be a number')
            exit()
        from ciphers.transposition import TranspositionCipher
        print(TranspositionCipher.encrypt(data['-m'], key))
        sys.stdout.flush()
    



if first == 'decrypt':

    try:
        opts, args = getopt(argv,'a:m:k:')
    except GetoptError as err:
        print(err)
    
    data = dict(opts)
    algorithm = data['-a']
    crypt = data['-m']
    key= data['-k']

    if algorithm == 'ceasar':
        try:
            key = int(key)
        except Exception as e:
            print('Key has to be a number')
            exit()
        from ciphers.ceasar import CeasarCipher
        print(CeasarCipher.decrypt(crypt, key))
        sys.stdout.flush()

    elif algorithm == 'vigenere':
        from ciphers.vigenere import VigenereCipher
        print(VigenereCipher.decrypt(crypt,key))
        sys.stdout.flush()


    elif algorithm == 'substitution':
        from ciphers.substitution import SubstitutionCipher
        alphabets = key.split(' ')[::-1]
        print(SubstitutionCipher.decrypt(crypt,*alphabets))
        sys.stdout.flush()

    elif algorithm == 'crack_vigenere':
        from ciphers.vigenere_crack import crack_vigenere
        key_length, user_limit = key.split(' ')
        result = crack_vigenere(crypt, int(key_length), int(user_limit))
        import json
        print(json.dumps(result))
        sys.stdout.flush()


if first == '--help':
    print("""
    Cryptography utility

    python main.py MODE [OPTIONS]

    MODE: encrypt|decrypt

    OPTIONS:
        -a Algorithm used to either encrypt or decrypt the message
        -m Message needed to be encrypted to decrypted
        -k The Key to either decrypt or encrypt the message
    
    EXAMPLES

        ceasar: python main.py encrypt -a ceasar -m "hello world" -k 6
        substitution: python main.py encrypt -a substitution -m "The quick brown fox jumps over the lazy dog." -k "zyxwvutsrqponmlkjihgfedcba"
    
    SPECIAL CASES:
        if ANY of the option arguments (-a or -m or -k) contain a space, put them in quotes
        in the SUBSTITUTION algorithm the key is the cipher Alphabet followed by the plaintext alphabet separated by a space,
        if the plaintext alphabet is the regular alphabet it can be omitted
    
    """)