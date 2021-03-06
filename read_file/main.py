"""
This program is to know how often each letter appears in the text
and print a simple histogram in alphabetical order
one text file has been provided: read_file/source_file.txt


"""


from os import strerror
srcname = input("Enter the source file name: ")
try:
    src = open(srcname,'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))

char = src.read(1).lower()
dict1 = {}
while char != "":
    if char >= 'a' and char <= "z":
        if char not in list(dict1.keys()):
             dict1[char] = 1
        else:
            dict1[char] += 1
    char = src.read(1).lower()

src.close()
str = ""

for key,value in sorted(dict1.items()):
    str +=f"{key} -> {value} \n"
print(str)
        
     