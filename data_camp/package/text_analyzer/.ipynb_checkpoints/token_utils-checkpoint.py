def tokenize(text, delimiter = ' '):
    """Split text by delimiter."""
    
    if text == '':
        text_list = list()
    else:
        text_list = text.split(delimiter)
        
    return text_list