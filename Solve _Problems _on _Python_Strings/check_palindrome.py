#!/usr/bin/python3

def check_palindrome(string):
    """Function that check if the value passed
    is palindrome.

    Args:
        string (list): value to check.

    Returns:
        True if is palindrome else return False.
    """
    if isinstance(string, int):
        string = str(string)
    lenght = len(string)
    for i in range(0,lenght):
        if string[i] != string[(i+1)*-1]:
            return False
    return True
