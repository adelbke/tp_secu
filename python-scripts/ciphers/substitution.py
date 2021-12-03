

class SubstitutionCipher:

    @classmethod
    def _uniqueChars(cls,text:str) -> bool:
        st = sorted(text)
        prev = ''
        for i in st:
            if prev == i:
                return False
            else:
                prev = i
        
        return True


    @classmethod
    def encrypt(cls,message:str, cipherAlphabet:str, plainAlphabet:str='abcdefghijklmnopqrstuvwxyz'):
        # if not cls._uniqueChars(plainAlphabet) or not cls._uniqueChars(cipherAlphabet):
        #     raise Exception('Cipher Alphabet and/or Plain Alphabet not unique')
        if len(plainAlphabet) != len(cipherAlphabet):
            raise Exception('Cipher Alphabet and Plain Alphabet have different lengths')
        
        plainAlphabet = plainAlphabet.lower() + plainAlphabet.upper()
        cipherAlphabet = cipherAlphabet.lower() + cipherAlphabet.upper()
        
        output = ''
        for i in message:
            index = plainAlphabet.find(i)
            if index != -1:
                output+= cipherAlphabet[index]
            else:
                output+=i
        
        return output

    @classmethod
    def decrypt(cls, cipher:str, cipherAlphabet:str, plainAlphabet:str='abcdefghijklmnopqrstuvwxyz'):
        return cls.encrypt(cipher, plainAlphabet, cipherAlphabet)
    

# message= 'The quick brown fox jumps over the lazy dog.'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# cipherAlphabet='zyxwvutsrqponmlkjihgfedcba'

# crypted= SubstitutionCipher.encrypt(message,cipherAlphabet)
# decrypt = SubstitutionCipher.decrypt(crypted, cipherAlphabet)
# print(f'{message} => {crypted} => {decrypt}')


# TODO: test it
# TODO: make it lower and uppercase
# first = SubstitutionCipher._uniqueChars('abcde')
# second = SubstitutionCipher._uniqueChars('abcdea')
# print((first, second))