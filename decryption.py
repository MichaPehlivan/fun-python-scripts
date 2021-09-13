#brute force algorithm for decrypting the affiene cipher
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

text = input("text to decrypt: ").replace(" ", "").upper()

possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

for a in possible_a:
    for b in range(0, 25):
        print(f"{a}, {b}: ")
        for i in text:
            index = alphabet.index(i)
            newindex = (a * index + b) % 26
            print(alphabet[newindex], end="")
        print("\n")

input()
