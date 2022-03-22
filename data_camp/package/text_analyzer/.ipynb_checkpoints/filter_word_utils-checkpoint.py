def filter_word_counts(word_dict, first_char):
    """Filter the list of words with first character."""
    dict = {}
    for key, value in word_dict.items():
        if first_char in key:
            dict[key] = value
    return dict

