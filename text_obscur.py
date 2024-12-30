#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Text Obfuscation
Description: Contains functions to manipulate and process text through splitting and rearranging words.

Functions:
- split_word(word): Splits a word into two halves.
- reverse_word(word): Rearranges a word by reversing its halves.
- revert_word(word): Restores the original arrangement of a reversed word.
- process_sentence(sentence, inverse): Processes each word in a sentence using either `reverse_word` or `revert_word`.


"""

def split_word(word):
    """
    Splits a word into two halves.

    Args:
        word (str): The word to be split.

    Returns:
        tuple: Two halves of the word. If the word length is odd, the middle character stays with the first half.
    """
    middle = len(word) // 2

    if len(word) % 2 == 0:
        return word[middle:], word[:middle]
    else:
        return word[middle:-1], word[:middle] + word[-1]

def reverse_word(word):
    """
    Rearranges a word by reversing its halves.

    Args:
        word (str): The word to be rearranged.

    Returns:
        str: The rearranged word.
    """
    first, second = split_word(word)
    return first + second

def revert_word(word):
    """
    Restores the original arrangement of a reversed word.

    Args:
        word (str): The reversed word to be restored.

    Returns:
        str: The original word.
    """
    first, second = split_word(word)
    return first + second

def process_sentence(sentence, inverse):
    """
    Processes each word in a sentence using either `reverse_word` or `revert_word`.

    Args:
        sentence (str): The sentence to be processed.
        inverse (bool): If True, applies `reverse_word`. Otherwise, applies `revert_word`.

    Returns:
        str: The processed sentence.
    """
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    if inverse:
        return " ".join([reverse_word(word) for word in sentence.split(" ")])
    else:
        return " ".join([revert_word(word) for word in sentence.split(" ")])


