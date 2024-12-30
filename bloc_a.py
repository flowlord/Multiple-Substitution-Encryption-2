#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Block A
Description: Performs a series of operations on a string to transform or restore the input text.

Functions:
- complexify(plain_text): Transforms the input text by reversing it and applying the `process_sentence` function.
- decomplexify(coded_text): Restores the original text by reversing the operations in `complexify`.

Dependencies:
- Requires `process_sentence` from the `text_obscur` module.


"""

from text_obscur import process_sentence

def complexify(plain_text):
    """
    Transforms the input text by reversing it and applying additional processing.

    Args:
        plain_text (str): The text to be transformed.

    Returns:
        str: The transformed text.
    """
    if not isinstance(plain_text, str):
        raise ValueError("Input must be a string.")

    plain_text = plain_text[::-1]  # Reverse the text
    plain_text = process_sentence(plain_text, True)  # Apply additional processing

    return plain_text

def decomplexify(coded_text):
    """
    Restores the original text by reversing the operations in `complexify`.

    Args:
        coded_text (str): The text to be restored.

    Returns:
        str: The original text.
    """
    if not isinstance(coded_text, str):
        raise ValueError("Input must be a string.")

    coded_text = process_sentence(coded_text, False)  # Reverse the processing
    coded_text = coded_text[::-1]  # Reverse the text

    return coded_text
