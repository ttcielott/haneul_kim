from .my_socialmedia import SocialMedia
from .filter_lines_utils import filter_lines

class Tweets(SocialMedia):
    def __init__(self, text):
        super().__init__(text)  # call the __init__ method of the parent class (Document clas)
        self.retweets = self._process_retweets()
    
    def _process_retweets(self):
        retweet_text = filter_lines(self.text, first_char = 'RT')
        
        return SocialMedia(retweet_text)
    
