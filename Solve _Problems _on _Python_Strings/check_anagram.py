#!/usr/bin/python3

def check_anagram(word1, word2):
    """Function that check if a word is
    anagram.

    Args:
        word1 (str): word to check.
        word2 (str): word to check.
    
    Attribute:
        check_list (list): each letter of
        the word will be added here.

    Returns:
        True if is anagram else return False.
    """
    check_list = [x for x in word2]
    for char in word1:
        if char in check_list:
            check_list.remove(char)
    return len(check_list) == 0

