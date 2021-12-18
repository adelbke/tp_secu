from .cipher import Cipher

class VigenereCipher:

    @classmethod
    def encrypt(cls, message:str, key:str):
        output = ''
        decalageCoef = 0

        for i in range(len(message)):
            keyindex = (i - decalageCoef ) % len(key)  if i >= len(key) else i - decalageCoef

            # print(f"le clé de {message[i]} a une clé de {key[keyindex]}")

            crypt = ord(key[keyindex]) - Cipher.getBounds(key[keyindex])[0]

            if message[i].isalpha():
                output += Cipher.shift(message[i], crypt)
            else:
                decalageCoef+=1
                output+= message[i]
        
        return output
    
    @classmethod
    def decrypt(cls, crypt:str, key:str):
        output = ''
        decalageCoef = 0

        for i in range(len(crypt)):
            keyindex = (i - decalageCoef ) % len(key)  if i >= len(key) else i - decalageCoef

            # print(f"le clé de {crypt[i]} a une clé de {key[keyindex]}")

            shiftValue = ord(key[keyindex]) - Cipher.getBounds(key[keyindex])[0]

            if crypt[i].isalpha():
                output += Cipher.shift(crypt[i], -shiftValue)
            else:
                decalageCoef+=1
                output+= crypt[i]
        
        return output



# msg, key = "The q[uick brown fox jumps over the lazy dog", 'cryptii'
# crypt = VigenereCipher.encrypt(msg, key)
# decrypt = VigenereCipher.decrypt(crypt, key)



# print(f"{msg} => {crypt} => {decrypt}")

