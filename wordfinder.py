"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    ...

    def __init__(self, file):
        words_file = open(file)
        self.words = self.clean(words_file)
        print(f"{len(self.words)} words read")

    def clean(self, words_file):
        return [word.strip() for word in words_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def omit_comments(self, words_file):
        return [
            word.strip()
            for word in words_file
            if word.strip() and not word.startswith("#")
        ]
