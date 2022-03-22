from text_analyzer import SocialMedia

def test_social_media_hashtags():
    
    social = SocialMedia('#coffee #coffeelover #coffeetime @somanydana')
    assert social.hashtag_counts == {'#coffee': 1, '#coffeelover':1, '#coffeetime':1}

test_social_media_hashtags()