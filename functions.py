import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.
    
    Parameters:
    lst (list): The input list.
    
    Returns:
    list: A new list with unique elements from the input list.
    """
    return list(set(lst))


def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.
    
    Parameters:
    string (str): The string to count uppercase and lowercase letters in.
    
    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.
    
    Returns:
    str: The sentence without any punctuation marks.
    """
    return sentence.translate(str.maketrans('', '', string.punctuation))


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.
    
    Returns:
    int: The number of words in the sentence.
    """
    sentence_no_punctuation = remove_punctuation_f(sentence)
    words = sentence_no_punctuation.split()
    return len(words)
