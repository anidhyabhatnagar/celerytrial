from time import sleep


class Stats:

    def __init__(self, word):
        self.word = word

    def char_count(self):
        count = 0
        for char in self.word:
            count = count + 1
        sleep(15)
        return count

    def vowel_count(self):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in self.word:
            if char in vowels:
                count = count + 1
        sleep(15)
        return count
