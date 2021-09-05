#Python script for Affiene encryption

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
inputstring = input("enter string: ").replace(" ", "").upper()

def newChar(char):
    index = alphabet.index(char)
    index = a * index + b

    while(index > 25):
        index %= 26

    return alphabet[index]

def encrypt(string):
    newString = ""
    for i in string:
        newString += newChar(i)

    return newString

print(encrypt(inputstring))
input()