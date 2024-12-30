# MULTIPLE SUBSTITUTION ENCRYPTION PROJECT (MSE)

Encryption software using multiple substitution with obfuscation, designed for creating puzzle and search games.

## Version Information
- **Version Name:** MSE-V28000 [ JOSH ]
- **Author:** Enron Group
- **Version:** 28.0.0
- **Release Date:** January 30, 2024

---

## Updates
### MSE-V28000
- General code improvement and optimization.

---

## Introduction
The Multiple Substitution Encryption (MSE) program is designed to encrypt text using three levels of character substitution and complexity. Developed since January 22, 2019, it offers a unique approach to text encryption.

### Character Database (BDC)
The files `all.txt`, `light_weight.txt`, and `ultra_light_weight.txt` contain characters used for substitution. These characters are divided into two groups:

- **Group A:** Used to generate substitution keys.
- **Group B:** Adds characters after substitution.

Each user's encryption becomes unique when encrypting a message for the first time.

- The program begins by importing essential libraries and characters from the BDC file, including lowercase and uppercase letters, numbers, punctuation, and accented characters.
- Configuration parameters are loaded from `setting.json`, specifying the character set for encryption, inclusion of punctuation, numbers, accents, and other settings.
- Parameters include:
  - Length of character groups used for substitution.
  - Length of special characters (a smaller group of characters is chosen).
  - Number of keys.
  - Shifting factors.

---

## Pseudo-Random Parameter Generator
The program can generate pseudo-random parameters (`setting.json`). Users can opt for creating random configurations.

Before substitution, the program applies several operations on the text, making it complex to decrypt.

---

## Encryption
### Core Process
The basic encryption process includes three steps:
1. Obscure the text by dividing it in two, rearranging characters, and applying additional transformations to increase complexity.
2. Substitute characters based on encryption keys generated from the BDC character set.
3. Introduce characters at pseudo-random positions in the text from the distinct Group B.

---

## Key Library Generation
The program generates a library of substitution keys chosen from Group A.

---

## Tools
The `tools.py` file provides essential tools such as:
- Generating a new BDC.
- Deleting encryption keys.
- Shuffling characters in the current BDC file.
- Cleaning and removing duplicates from the BDC file.

---

## Demo and Usage
![Demo Example](exemple/captur_demo.PNG)

Try the Google Colab preview: [here](https://colab.research.google.com/drive/1WWT81_UlmaZ9kKG6FbfdQ-ac4muXzYBf?usp=sharing)

---

_This is just the foundation of the code. Look at the code from another perspective, and you can see billions of possibilities!_

<center>The wonderful world of secrets, letters, and numbers!</center>




