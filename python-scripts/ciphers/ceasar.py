
from .cipher import Cipher

class CeasarCipher(Cipher):

    @classmethod
    def encrypt(cls,message, key):
        words = message.split(' ')
        output = ''
        for word in words:
            for i in word:
                if i.isalpha():
                    output += cls.shift(i,key)
                else:
                    output += i
            output+= ' '

        return output
        
    
    @classmethod
    def decrypt(cls,crypted:str, key:int):
        return CeasarCipher.encrypt(crypted, -key)




# msg, shift = "The qu[ick brown fox jumps over the lazy dog", 7
# crypt = CeasarCipher.encrypt(msg, shift)
# decrypt = CeasarCipher.decrypt(crypt, shift)


# print(f"{msg} => {crypt} => {decrypt}")

