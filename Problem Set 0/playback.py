# Richard Phan
# 11/8/25

"""
Instructions: Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

"""

#Goal: this program mimics a YT playback slowdown. Spaces in an inputted string is replaced with ...

slowed_sentence = input("Enter a sentence: ")
print(slowed_sentence.replace(" ", "...")) #.replace(old, new)

