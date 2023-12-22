names = []
ages = []

with open('DOB.txt', 'r') as file:
    for line in file:
        words = line.split(" ")
        names.append(words[0] + " " + words[1])
        ages.append(words[2] + " " + words[3] + " " + words[4].strip("\n"))        

print("\nNames\n")
for name in names:
    print(name)

print("\nAges\n")
for age in ages:
    print(age)





# with open('DOB.txt', 'r') as file:
#     for line in file:
#         for index, value in enumerate(line):
#             if value.isnumeric():
#                 names.append(line[0: index - 1])
#                 ages.append(line[index: len(line) - 1])
#                 break








# print("\nNames\n")

# with open('DOB.txt', 'r') as file:
#     for line in file:
#         name = ""
#         for index, value in enumerate(line):
#             if not value.isnumeric():
#                 name += value
#             else:
#                 print(name[:-1])
#                 break

# print("\Ages\n")

# with open('DOB.txt', 'r') as file:
#     for line in file:
#         age = ""
#         spaces = 0
#         line.reverse()
#         for index, value in enumerate(line):
#             if spaces == 3:
#                 print(age[:-2]) #print reverse
#                 break                
#             elif value == " ":
#                 spaces += 1
#             age += value