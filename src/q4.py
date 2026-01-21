"""
Please implement this stub function to match the documentation.
As always, make sure to implement tests in the tests directory.
"""

from typing import Optional


def most_common_letter(s: str) -> Optional[str]:
    """Finds the most common letter in a given string.
    
    Parameters
    ----------
    s : str
        The input string
    
    Returns
    -------
    Optional[str]
        The most common letter in the string. If there is a tie, return the 
        letter that comes first alphabetically.
        Ignore case -- 'a' is equal to 'A'. Non-letter characters should be ignored.
        If there are no letters in the string, return None.
    """
    letter_counts = {}
    
    for letter in s:
        if letter.isalpha():
            lower_letter = letter.lower()
            if lower_letter in letter_counts:
                letter_counts[lower_letter] += 1
            else:
                letter_counts[lower_letter] = 1
    
    
    if len(letter_counts) == 0:
        return None
    
   
    max_count = 0
    most_common = None
    

    sorted_letters = sorted(letter_counts.keys())
    
    for letter in sorted_letters:
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
            most_common = letter
    
    return most_common
