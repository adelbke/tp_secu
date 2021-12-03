

class Cipher:

    @classmethod
    def shift(cls,letter:str, shiftValue:int):
        minimum, maximum = Cipher.getBounds(letter)
        decalage = ord(letter) + shiftValue
        if decalage > maximum:
            decalage = (decalage - minimum) % (maximum - minimum + 1) + minimum
        if decalage < minimum:
            decalage = maximum - (minimum - decalage - 1)
        return chr(decalage)
    
    @classmethod
    def getBounds(cls, letter:str):
        if letter.islower():
            maximum, minimum = ord('z'), ord('a')
        if letter.isupper():
            maximum, minimum = ord('Z'), ord('A')
        
        return minimum, maximum