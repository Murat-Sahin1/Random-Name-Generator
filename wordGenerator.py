import random as rn


class wordGenerator:
    def __init__(self, _word_length):
        self.word_length = _word_length
        self.banned_letters = []
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
        new_word = self.merge_word(self.word_length)
        print(new_word)

    def merge_word(self, iteration):
        word = ''
        temp = rn.randint(65, 90)
        banned_letter_search = False
        #  self.banned_letters.append()
        # while :
        # temp = rn.randint(65, 90)

        for i in range(0, iteration):
            if i > 0:
                temp = rn.randint(65, 90)
                for banned_letter in self.banned_letters:
                    print("Rastgele gelen harf: ", self.word_bank[temp], "Yasaklı harf: ", self.banned_letters[0])
                    if self.word_bank[temp] == banned_letter:
                        # Kelimede bulunan son harfe eklemek üzere yasaklı bir harf bulundu.
                        print("Found a banned letter: ", banned_letter, self.word_bank[temp])
                        while self.word_bank[temp] == banned_letter:
                            print("Getting a new letter...")
                            temp = rn.randint(65, 90)
                        print("Current letters: ", banned_letter, self.word_bank[temp])
                # Now, I have a different value than the banned letter, let's add it to the word and
                # Change my next banned letters
                self.banned_letters = self.find_banned_letters(temp)
                word += self.word_bank[temp]
            else:
                # For the first letter, it doesn't matter which letter we use.
                self.banned_letters = self.find_banned_letters(temp)
                word += self.word_bank[temp]
        return word

    def find_banned_letters(self, _letter):
        for i in self.excluded_letters:
            if i[0] == _letter:
                val = i[1:]
                return val

    def get_phonetic(self):
        my_phonetic_input = [
            [65, 'I', 'J', 'O', 'W', 'Y'],  # A

            [66, 'C', 'F', 'J', 'M', 'N', 'P', 'Q', 'S', 'W'],  # B

            [67, 'B', 'D', 'F', 'G', 'H', 'P', 'Q', 'S', 'V', 'W', 'Y', 'Z'],  # C

            [68, 'B', 'C', 'L', 'K', 'M', 'N', 'P', 'Q', 'T', 'Y', 'Z'],  # D

            [69, 'I', 'O', 'Q', 'U'],  # E

            [70, 'B', 'G', 'J', 'M', 'N', 'P', 'S', 'V', 'W', 'X', 'Y', 'Z'],  # F

            [71, 'D', 'J', 'L', 'K', 'M', 'N', 'Q', 'V', 'X', 'Y'],  # G

            [72, 'B', 'C', 'D', 'F', 'G', 'M', 'N', 'P', 'S', 'T', 'V', 'W', 'X', 'Z'],  # H

            [73, 'C', 'D', 'H', 'O', 'Q', 'Y'],  # I

            [74, 'G', 'H', 'L', 'K', 'Q', 'S', 'W', 'Z'],  # J

            [75, 'B', 'C', 'D', 'J', 'P', 'R', 'S', 'V', 'W'],  # K

            [76, 'B', 'F', 'G', 'H', 'J', 'P', 'S', 'V', 'W', 'Z'],  # L

            [77, 'C', 'F', 'G', 'O', 'Q', 'U', 'X', 'Y', 'Z'],  # M

            [78, 'B', 'D', 'F', 'G', 'L', 'K', 'P', 'Q', 'Y'],  # N

            [79, 'E', 'F', 'I', 'J', 'Q', 'S', 'T', 'U', 'W'],  # O

            [80, 'B', 'C', 'D', 'G', 'I', 'K', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'X', 'P'],  # P

            [81, 'Q', 'B', 'C', 'D', 'G', 'I', 'J', 'K', 'O', 'U', 'V', 'X'],  # Q

            [82, 'B', 'F', 'G', 'H', 'J', 'M', 'N', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],  # R

            [83, 'C', 'F', 'G', 'H', 'P', 'Q', 'R', 'T', 'V', 'W', 'X', 'Y', 'Z'],  # S

            [84, 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'P', 'Q', 'W', 'Y'],  # T

            [85, 'E', 'I', 'O', 'Q', 'Y', 'Z'],  # U

            [86, 'B', 'F', 'G', 'I', 'J', 'K', 'P', 'Q', 'T', 'Y', 'Z'],  # V

            [87, 'D', 'C', 'F', 'G', 'H', 'J', 'N', 'P', 'Q', 'V', 'W', 'X', 'Z'],  # W

            [88, 'B', 'D', 'G', 'J', 'K', 'M', 'P', 'Q', 'S', 'V', 'W', 'Z'],  # X

            [89, 'B', 'C', 'G', 'J', 'K', 'M', 'P', 'Q', 'S', 'W', 'X'],  # Y

            [90, 'B', 'D', 'G', 'H', 'J', 'M', 'N', 'P', 'Q', 'S', 'Y']]  # Z
        return my_phonetic_input
