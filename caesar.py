#!/usr/bin/python3

from sys import exit,argv

class caesarCipher :
    teks = None

    def __init__(self, text, shift):
        self.text = text
        self.shift = shift

    def caesarDecrypt(self):
        cipher = self.text
        shifts = self.shift
        plains = ""

        for char in cipher :
            if char.isspace() or (not char.isalpha()):
                plains += char
            elif char.isupper():
                plains += chr((ord(char) - shifts - 65) % 26 + 65)
            else:
                plains += chr((ord(char) - shifts - 97) % 26 + 97)
        else:
            caesarCipher.teks = plains

    def __repr__(self):
        return caesarCipher.teks

print(
"""                         _____         _
 ___ ___ ___ ___ ___ ___| __  |___ _ _| |_ ___
|  _| .'| -_|_ -| .'|  _| __ -|  _| | |  _| -_|
|___|__,|___|___|__,|_| |_____|_| |___|_| |___|
[ Caesar Cipher Brute Forcer ]""")

if len(argv) != 2 :
    print("[ ./caesar.py <ciphertext string> ]")
    exit()
else:
    string = argv[1]

print()

for shift in range(1,27):
    caesar = caesarCipher(string,shift)
    caesar.caesarDecrypt()
    print(shift, caesar, sep = " : ")
