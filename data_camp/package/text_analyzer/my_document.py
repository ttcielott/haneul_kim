from .token_utils import tokenize
from collections import Counter

class Document:
    """Tokenize the document by delimiter and count the number of words"""
    def __init__(self, text):
        self.text = text
        # tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        
        # perform word count with non-public count-words method
        self.word_counts = self._count_words()
        
    def _tokenize(self):
        return tokenize(self.text)
    
    def _count_words(self):
        return Counter(self.tokens)