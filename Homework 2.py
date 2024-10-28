# Donovan Appelhans
# UWYO COSC 1010
# 10/28/2024
# HW 02
# Lab Section: 12
# Sources, people worked with, help given to: 
# Ezra Visser

code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

def morse_trans(input_text):
    morsecode = []
    for char in input_text.upper():
        if char in code_dict:
            morsecode.append(code_dict[char])
    return ' '.join(morsecode)

text_input = input('enter text to translate')
code_out = morse_trans(text_input)
print(code_out)