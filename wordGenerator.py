import random as rn


class wordGenerator:
    def __init__(self, _word_length):
        self.word_length = _word_length
        self.my_random_number = rn.randint(65, 90)
        self.word_bank = {65: 'A', 66: 'B',
                          67: 'C', 68: 'D',
                          69: 'E', 70: 'F',
                          71: 'G', 72: 'H',
                          73: 'I', 74: 'J',
                          75: 'K', 76: 'L',
                          77: 'M', 78: 'N',
                          79: 'O', 80: 'P',
                          81: 'Q', 82: 'R',
                          83: 'S', 84: 'T',
                          85: 'U', 86: 'V',
                          87: 'W', 88: 'X',
                          89: 'Y', 90: 'Z'}
        new_word = self.get_word(self.word_length)
        print(new_word)

    def get_word(self, iteration):
        word = ''
        for i in range(0, iteration):
            temp = rn.randint(65, 90)
            word += self.word_bank[temp]
        return word
