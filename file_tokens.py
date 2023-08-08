# Jeremiah Kent
# 2023-08-07

from nltk import word_tokenize

class FileTokens:
    """Extract tokens from a file.

        Instantiate with a filename indicating a text corpus.
        Tokens will immediately be extracted from the file, as lowercase, excluding punctuation and whitespace.
    """
    def __init__(self, file_name):
        file_content = open(file_name).read()
        tokens = word_tokenize(file_content)
        self.words = [word.lower() for word in tokens if word.isalpha()]

    def tokens(self):
        """ Retrieve the extracted list of tokens """
        return self.words

