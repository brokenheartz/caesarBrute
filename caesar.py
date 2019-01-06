#!/usr/bin/python3

from sys import exit,argv
from colorama import Fore, Style
import os, random

class caesarCipher :
    teks = None

    def __init__(self, text, shift):
        self.text = text
        self.shift = shift
        self.caesarDecrypt()

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

def createOutput(fileName, fileContent):
    folderName = "output"
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    fileName = folderName + "/" + fileName
    createFile = open(fileName,"w")
    createFile.write(fileContent)
    createFile.close()
    if os.path.exists(fileName):
        return True
    else:
        return False

print( Style.BRIGHT + Fore.WHITE +
"""                         _____         _
 ___ ___ ___ ___ ___ ___| __  |___ _ _| |_ ___
|  _| .'| -_|_ -| .'|  _| __ -|  _| | |  _| -_|
|___|__,|___|___|__,|_| |_____|_| |___|_| |___|
""" + Fore.RED +
"[ Caesar Cipher Brute Forcer ]".strip())

color = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.WHITE,
    Style.BRIGHT + Fore.GREEN,
    Style.BRIGHT + Fore.YELLOW,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.MAGENTA
]

if len(argv) != 2 :
    print("[ ./caesar.py <cipher text/file> ]")
    exit()
else:
    userArg = argv[1]

if os.path.isfile(userArg):
    cipherString = open(userArg,"r").read()
    createFile = True
else:
    cipherString = userArg
    createFile = False

print()

for shift in range(26):
    ranNumber = random.randint(0,5)
    caesar = caesarCipher(cipherString,shift + 1)
    if createFile:
        fileName = "shift%d.txt" % (shift + 1)
        file = createOutput(fileName,str(caesar))
        if file :
            print(color[ranNumber] + "Creating", fileName, "succesful!")
        else:
            print("Fail to create", fileName)
    else:
        print(color[ranNumber],shift + 1, " : ",caesar)
