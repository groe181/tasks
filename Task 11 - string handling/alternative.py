string = "I am an example string to test"
new_string = ""

for index, char in enumerate(string):
    if index % 2 == 0:
        new_string += char.upper()
    else:
        new_string += char.lower()

print(new_string)

words = string.split()

for index, word in enumerate(words):
    if index % 2 == 0:
        words[index] = word.upper()
    else:
        words[index] = word.lower()

print(" ".join(words))
