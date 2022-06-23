"""
Write a function which behaves almost exactly like the original split() method.


"""
def mysplit(strng):
    myList = []
    letter = ""
    strng = strng.lstrip()
    if not strng.endswith(" "):
        strng += " "
    for char in strng:
        if char == " ":
            myList.append(letter)
            letter = ""
        else:
            letter += char
    return myList

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))