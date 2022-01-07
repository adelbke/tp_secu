
from ciphers.vigenere import VigenereCipher
from itertools import product


class AlphabetFrequency:

  def __init__(self, data=None, classic=False):
    self._frequencies = []
    self._occurences = []
    if classic:
      self.occurences_changed = False
      self._frequencies = [
        ('A',	8.13),('B',	0.93),('C',	3.15),('D',	3.55),('E',	15.10),('F',	0.96),('G',	0.97),
        ('H',	1.08),('I',	6.94),('J',	0.71),('K',	0.16),('L',	5.68),('M',	3.23),('N',	6.42),('O',	5.27),
        ('P',	3.03),('Q',	0.89),('R',	6.43),('S',	7.91),('T',	7.11),('U',	6.05),('V',	1.83),
        ('W',	0.04),('X',	0.42),('Y',	0.19),('Z',	0.21)
      ]
      self._frequencies = [(x[0].lower, x[1]/100) for x in self._frequencies]
    if data == None:
      self.occurences_changed = False
      for i in range(ord('a'), ord('z') + 1):
        self.occurences.append((chr(i), 0))
    else:
      dictionaryData = dict(data)
      self.occurences_changed = True
      for i in range(ord('a'), ord('z') + 1):
        occurence = dictionaryData.get(chr(i))
        if occurence != None:
          self.occurences.append((chr(i),occurence))
        else:
          self.occurences.append((chr(i), 0))
  
  @property
  def occurences(self):
    return self._occurences
  
  @occurences.setter
  def occurences(self, val):
    self.occurences_changed = True
    self._occurences = val

  @property
  def total_occurences(self):
    return sum([x[1] for x in self.occurences])
  
  @property
  def frequencies(self):
    if self.occurences_changed:
      self._frequencies = []
      total = self.total_occurences
      for i in range(self.length):
        self._frequencies.append((self.occurences[i][0], self.occurences[i][1] / total))
    return self._frequencies
  
  
  @property
  def length(self):
    return len(self.occurences)
  
  def shift(self, direction:str):
    self.occurences_changed = True
    if direction == 'right':
      n = len(self.occurences)
      self.occurences.insert(0,self.occurences[-1])
      self.occurences = self.occurences[:n]
    elif direction == 'left':
      self.occurences.append(self.occurences[0])
      self.occurences = self.occurences[1:]
  

  def shiftRight(self):
    self.shift('right')
  
  def shiftLeft(self):
    self.shift('left')
  
  def best_match_shift(self, secondAlphabet, matches_count=5):
    scores = []
    for i in range(self.length):
      scores.append(self._compare(secondAlphabet))
      self.shiftLeft()
    shift_scores = [(i, scores[i]) for i in range(len(scores))]
    output = sorted(shift_scores, key= lambda x: x[1], reverse=True)
    return output[:matches_count]

  def _compare(self, secondAlphabet):
    proximity = 0
    for i in range(self.length):
      proximity += self.frequencies[i][1] * secondAlphabet.frequencies[i][1]
    return proximity
  

def groupSameShift(crypt:str, keySize:int):
    output=[[] for x in range(keySize)]
    for i in range(len(crypt)):
        keyindex = i % keySize  if i >= keySize else i
        output[keyindex].append(crypt[i])
    return output


def getMostFrequent(letters:list):
    counts={}
    for letter in letters:
        if counts.get(letter) == None:
            counts[letter] = 1
        else:
            counts[letter]+= 1
    
    count_sum = sum(counts.values())
    for key in counts:
      counts[key] = counts[key] / count_sum
    sorted_x = sorted(counts.items(), key=lambda kv: kv[0])
    return list(sorted_x)


def crack_vigenere(crypt, key_length, user_limit=81):

  crypt= 'kjh hukfy visgovf nkjh julf urxclokvgk us poxshkis ubvq otv qfk us wxpdngxs jkkwnk'
  encrypted_message = ''.join(crypt.split(' '))

  lettersList = groupSameShift(encrypted_message,key_length)
  frequencyOrders = [getMostFrequent(x) for x in lettersList]

  max_chars = int((user_limit + 1)**(1/key_length))
  key_possibilities = []
  for order in frequencyOrders:
    french = AlphabetFrequency(classic=True)
    case = AlphabetFrequency(order)
    key_chars = [chr(ord('a') + x[0]) for x in case.best_match_shift(french, matches_count=max_chars)]
    key_possibilities.append(key_chars)

  # print(key_possibilities)
  # return
  possible_keys = []
  iteration = product(*tuple(key_possibilities))
  probable_key = next(iteration, None)
  i = 0
  while i < user_limit and probable_key is not None:
    key = ''.join(probable_key)
    possible_keys.append({ "msg": VigenereCipher.decrypt(crypt, key), "key": key})
    # possible_keys.append({ "key": key})
    probable_key = next(iteration, None)
    i+=1
  
  return possible_keys


# print(crack_vigenere('kjh hukfy visgovf nkjh julf urxclokvgk us poxshkis ubvq otv qfk us wxpdngxs jkkwnk', 4, 18))
