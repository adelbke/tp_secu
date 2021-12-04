from cipher import Cipher
from matrices import ipMatrix, pc1, pc2, shift_number, expansion_table, listSBox, fpermutation, ip_1

class DesCipher(Cipher):

    @classmethod
    def _bits_to_blocks(cls, bits:str):
        blocks = []
        for i in range(0,len(bits),64):
            if i+64 < len(bits) -1:
                block = bits[i:i+64]
            else:
                # TODO: add block fill handling
                block = bits[i:i+64]
            
            blocks.append(block)
    
    @classmethod
    def _ip(cls,block:str):
        if len(block) != 64:
            raise Exception('passed Block length is not 64bits')
        return cls._apply_table(block,ipMatrix)
    
    # applies table shift to a bit list
    @classmethod
    def _apply_table(cls, text:str, table:list, index_starts=1):
        outbounds = filter(lambda x: x - index_starts > len(text) -1,table)
        if len(list(outbounds)) > 0:
            raise Exception('Table applied contains out of bounds values')
        scribbled = ''
        for i in range(len(table)):
            table_index= table[i]
            scribbled+=text[table_index-index_starts]
        return scribbled
    
    @classmethod
    def _pc1(cls,key:str):
        if len(key) != 64:
            raise Exception('Key length should be 64 to generate 56 bit key')
        return cls._apply_table(key, pc1, index_starts=0)


    @classmethod
    def _lsi(cls, key:str, round:int):
        l, r = cls._cut_text(key)
        l= cls.shift_text(l,shift_number[round])
        r= cls.shift_text(r,shift_number[round])
        return l+r
    

    @classmethod
    def compression_permutation(cls, key:str):
        if len(key) != 64:
            raise Exception('Key length should be 64 to generate 48 bit keys')
        key_56 = cls._pc1(key)
        k = key_56
        key_rounds = []
        for i in range(16):
            k = cls._lsi(k, i)
            key_rounds.append(k)
            
        for i in range(len(key_rounds)):
            key_rounds[i] = cls._apply_table(key_rounds[i],pc2)
        
        return key_rounds

    @classmethod
    def xor(cls,a:str, b:str):
        result = ''
        for i in range(len(a)):
            result+= '1' if a[i] != b[i] else '0'
        return result
    

    @classmethod
    def _f(cls,halfBlock:str, subKey:str):
        expandedHalfBlock = cls._apply_table(halfBlock, expansion_table)
        tempResult = cls.xor(expandedHalfBlock, subKey)
        # print(tempResult)
        blocks = [tempResult[i:i+6] for i in range(0,len(tempResult),6)]
        def apply_sbox(block:str, sbox:list):
            column = int(block[1:-1],2)
            line = int(block[0] + block[-1],2)

            return bin(sbox[line][column])[2:].zfill(4)
        results = ''
        for i in range(len(blocks)):
            results += apply_sbox(blocks[i],listSBox[i])
        
        return cls._apply_table(results, fpermutation)


    @classmethod
    def encryption_round(cls,l:str, r:str, k:str):
        return cls.xor(l,cls._f(r,k))
    
    @classmethod
    def encrypt(cls,msg:str, key:str):
        msg_bits = cls.text_to_bits(msg)[:64] # one block
        key_bits = cls.text_to_bits(key)[:64] # one block
        # msg_bits = msg
        # key_bits = key
        key_rounds = cls.compression_permutation(key_bits)
        # print(f'Message: {msg_bits}')
        # print(f'IP: {cls._ip(msg_bits)}')
        l,r = cls._cut_text(cls._ip(msg_bits))
        
        for i in range(16):
            # print(f'L{i} = {l} / R{i} = {r}')
            newl = r
            r = cls.encryption_round(l,r,key_rounds[i])
            l = newl
        cryptedBinary = cls._apply_table(r+l,ip_1)
        return cls.bits_to_text(cryptedBinary)




# key_bits = DesCipher.text_to_bits('hello world')[:64]
# print(key_bits)
# keys_48 = DesCipher.compression_permutation('0001001100110100010101110111100110011011101111001101111111110001')

# e_k1 = DesCipher._f('11110000101010101111000010101010', '000110110000001011101111111111000111000001110010')
#key = DesCipher.bits_to_text(bits)
import pprint
# pprint.pprint(e_k1)
# print(key)

# m = '0000000100100011010001010110011110001001101010111100110111101111'
# k = '0001001100110100010101110111100110011011101111001101111111110001'

m = 'hello wo'
k = 'bonjourj'
r = DesCipher.encrypt(m,k)

pprint.pprint(r)