with open("./frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
chars = {}
for letter in file_contents:
    lcase = letter.lower()
    if lcase in chars:
        chars[lcase] += 1
    else:
        chars[lcase] = 1
for character in chars:
    print("Character " + character + " appeared " + str(chars[character]) + " times.")