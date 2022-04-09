import random as rn


class wordGenerator:
    def __init__(self, _word_length):
        self.word_length = _word_length
        self.excluded_letters = self.get_phonetic()
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

    def get_phonetic(self):
        my_phonetic_input = {
            'A': ['I', 'J', 'O', 'W', 'Y', ],

            'B': ['C', 'F', 'J', 'M', 'N', 'P', 'Q', 'S', 'W'],

            'C': ['B', 'D', 'F', 'G', 'H', 'P', 'Q', 'S', 'V', 'W', 'Y', 'Z'],

            'D': ['B', 'C', 'L', 'K', 'M', 'N', 'P', 'Q', 'T', 'Y', 'Z'],

            'E': ['I', 'O', 'Q', 'U'],

            'F': ['B', 'G', 'J', 'M', 'N', 'P', 'S', 'V', 'W', 'X', 'Y', 'Z'],

            'G': ['D', 'J', 'L', 'K', 'M', 'N', 'Q', 'V', 'X', 'Y'],

            'H': ['B', 'C', 'D', 'F', 'G', 'M', 'N', 'P', 'S', 'T', 'V', 'W', 'X', 'Z'],

            'I': ['C', 'D', 'H', 'O', 'Q', 'Y'],

            'J': ['G', 'H', 'L', 'K', 'Q', 'S', 'W', 'Z'],

            'L': ['B', 'F', 'G', 'H', 'J', 'P', 'S', 'V', 'W', 'Z'],

            'K': ['B', 'C', 'D', 'J', 'P', 'R', 'S', 'V', 'W'],

            'M': ['C', 'F', 'G', 'O', 'Q', 'U', 'X', 'Y', 'Z'],

            'N': ['B', 'D', 'F', 'G', 'L', 'K', 'P', 'Q', 'Y'],

            'O': ['E', 'F', 'I', 'J', 'Q', 'S', 'T', 'U', 'W'],

            'P': ['B', 'C', 'D', 'G', 'I', 'K', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'X', 'P'],

            'Q': ['Q', 'B', 'C', 'D', 'G', 'I', 'J', 'K', 'O', 'U', 'V', 'X'],

            'R': ['B', 'F', 'G', 'H', 'J', 'M', 'N', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

            'S': ['C', 'F', 'G', 'H', 'P', 'Q', 'R', 'T', 'V', 'W', 'X', 'Y', 'Z'],

            'T': ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'P', 'Q', 'W', 'Y'],

            'U': ['E', 'I', 'O', 'Q', 'Y', 'Z'],

            'V': ['B', 'F', 'G', 'I', 'J', 'K', 'P', 'Q', 'T', 'Y', 'Z'],

            'W': ['D', 'C', 'F', 'G', 'H', 'J', 'N', 'P', 'Q', 'V', 'W', 'X', 'Z'],

            'X': ['B', 'D', 'G', 'J', 'K', 'M', 'P', 'Q', 'S', 'V', 'W', 'Z'],

            'Y': ['B', 'C', 'G', 'J', 'K', 'M', 'P', 'Q', 'S', 'W', 'X'],

            'Z': ['B', 'D', 'G', 'H', 'J', 'M', 'N', 'P', 'Q', 'S', 'Y']}
        return my_phonetic_input

