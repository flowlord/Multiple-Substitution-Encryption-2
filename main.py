#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Main Interface
Description: Provides a demonstration and interface for the Multiple Substitution Encryption (MSE) system.

Functions:
- demo(): Demonstrates encryption and decryption using example sentences.


"""

from random import choice
from colorama import Fore, Style
from MSE import mse_cipher, mse_decipher

# Example sentences for demonstration
example_sentences = [
    "The sign said there was road work ahead so he decided to speed up.",
    "She couldn't understand why nobody else could see that the sky is full of cotton candy.",
    "They looked up at the sky and saw a million stars.",
    "He had a hidden stash underneath the floorboards in the back room of the house.",
    "He was surprised that his immense laziness was inspirational to others.",
    "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn.",
    "My Mum tries to be cool by saying that she likes all the same things that I do.",
    "She had some amazing news to share but nobody to share it with."
]

def demo():
    """
    Demonstrates the encryption and decryption process using random example sentences.
    """
    print("---------- * DEMO * ----------\n")

    print(Fore.RED + "Encrypted text:\n" + Style.RESET_ALL)
    message = mse_cipher(choice(example_sentences), True)

    print(message, "\n\n")

    print(Fore.GREEN + "Decrypted text:\n" + Style.RESET_ALL)
    print(mse_decipher(message, False))

# Uncomment the following line to run the demo
#demo()

# Uncomment these lines to manually encrypt and decrypt a custom message
# encrypted_message = mse_cipher("Your custom message here", True)
# print(encrypted_message)
# print(mse_decipher(encrypted_message, False))

# Uncomment this line to reset encryption keys
# reset()

