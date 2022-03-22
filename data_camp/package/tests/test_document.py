from text_analyzer import Document
from text_analyzer import Counter

def test_document_tokens():
    doc = Document('Hello. My Name is Dana.')
    
    assert doc.tokens == ['Hello.', 'My', 'Name', 'is', 'Dana.']
    

test_document_tokens()

# test edge case of blank document
def test_document_empty():
    doc = Document('')
    
    assert doc.tokens == []
    assert doc.word_counts == Counter()


test_document_empty()

# when testing class objects, it's not wise to compare two objects with double equals
Doc_a = Document('Loving you is a losing game.')
Doc_b = Document('Loving you is a losing game.')

# test with double equals
Doc_a == Doc_b

# instead, test like this
Doc_a.tokens == Doc_b.tokens