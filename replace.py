"""This program formats strings as required by practical task #2."""


ORIGINAL_SENTENCE = "The!quick!brown!fox!jumps!over!the!lazy!dog."


#Format the sentence by using the replace string method.
#This will change each instance of "!" with a blank space.
#Assign this value to a new variable so it can be re-used.
#Print this new variable.
FORMATTED_SENTENCE = ORIGINAL_SENTENCE.replace("!", " ")
print(FORMATTED_SENTENCE)


#Use the upper string method on FORMATTED_SENTENCE
#This will create a new value of FORMATTED_SENTENCE
#where each character is in uppercase.
#Print the returned value.
print(FORMATTED_SENTENCE.upper())


#Reverse the original sentence by slicing the string in full.
#This operation will start from the last index value
#and move one character at a time, right to left.
#Print the returned value
print(ORIGINAL_SENTENCE[::-1])

#I'm unsure if it is required to print the original sentence
#or the sentance that has been formatted without the "!" marks.
#In case it is the formatted sentance, then line 26 should be:
#print(FORMATTED_SENTENCE[::-1])
