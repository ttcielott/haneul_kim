def filter_lines(text, first_char):
    """Filter lines by beginning characters (case sensitive).
    
    :param text: multi-line text to filter
    :param first_char: required characters for line to start with to be returned
    :return: text with only lines starting with first_char included
    
    >>> text = 'santoki tokiya\nuhdileul ganunya\nkkangchong kkangchong'
    >>> filter_lines(text, 'u')
    'uhdileul ganunya'
    """
    result = ''
    line_list = text.split('\n')
    for l in line_list:
        if first_char in l:
            result += l + ' '
        else:
            pass
    return result
            