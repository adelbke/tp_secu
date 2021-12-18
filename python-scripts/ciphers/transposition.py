

class TranspositionCipher:

    @classmethod
    def encrypt(cls, message:str, key:int ):
        nbLines = int(len(message) / key) + 1
        matrix = [[None for y in range(key)] for x in range(nbLines)]
        # print(matrix)

        for i in range(len(message)):
            curLine = int(i / key)
            curCol = i % key
            # print(f'matrix[{curLine}][{curCol}]')
            matrix[curLine][curCol] = message[i]
        
        from pprint import pprint
        pprint(matrix)

        output = ''
        for j in range(key):
            for i in range(nbLines):
                if matrix[i][j] != None:
                    output += matrix[i][j]
        
        return output
    
    @classmethod
    def decrypt(cls, message:str, key:int):
        nbLines = int(len(message) / key) + 1
        matrix = [[None for y in range(nbLines)] for x in range(key)]
        # print(matrix)

        
        for i in range(len(message)):
            curLine = int(i / nbLines)
            curCol = i % nbLines
            
            matrix[curLine][curCol] = message[i]
        
        from pprint import pprint
        pprint(matrix)

        output = ''
        for j in range(nbLines):
            for i in range(key):
                if matrix[i][j] != None:
                    output += matrix[i][j]

        return output


# x= TranspositionCipher.encrypt('the quick brown fox jumps over the lazy dog', 5)
# print(x)

# print(TranspositionCipher.decrypt(x,5))
