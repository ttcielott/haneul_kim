# import parent class object
from .my_document import Document
from .filter_word_utils import filter_word_counts

# create a child class with inheritance
class SocialMedia(Document):
    def __init__(self, text):
        # call parent's __init__ method
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char = '#')
    
    def _count_mentions(self):
        # filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char = '@')
      