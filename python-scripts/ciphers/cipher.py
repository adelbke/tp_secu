

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
    
    @classmethod
    def text_to_bits(cls, text:str):
        binary_result = ''
        for character in text:
            
            # bits= '{0:b}'.format(ord(character))
            # bits = ''.join(['0' for i in range(8-len(bits))]) + bits
            # binary_result+=bits
            binary_result+=bin(ord(character))[2:].zfill(8)
        
        return binary_result
    
    @classmethod
    def bits_to_text(cls, bits:str):
        text = ''
        for i in range(0,len(bits),8):
            character = int(bits[i:i+8],2)
            text+= chr(character)
        
        return text
    
    @classmethod
    def _cut_text(cls, bits:str):
        if len(bits) % 2 != 0:
            raise Exception('bits passed have odd length, can\'t produce same-length left and right ')
        middle = int(len(bits)/2)
        return bits[:middle], bits[middle:]
    
    @classmethod
    def shift_text(cls, text:str, shift_value:int, side='left'):
        if side == 'left':
            output = text[shift_value:] + text[:shift_value]
        elif side == 'right':
            # TODO: code this
            raise Exception('Not implemented')
        return output
        

