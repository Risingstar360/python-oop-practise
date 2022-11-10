"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    ...
    def __init__(self, path="words.txt"):
        """Read dictionary and reports # items read."""

        words_file = open(path)

        self.words = self.parse(words_file)

        print(f"{len(self.words)} words have been read")

    def parse(self, words_file):
        """Parse the words_file to the list of words."""

        return [word.strip() for word in words_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

