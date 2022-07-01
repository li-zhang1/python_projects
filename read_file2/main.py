"""
This program is to know how often each letter appears in the text
the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
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

for key,value in sorted(dict1.items(), key = lambda x: x[1]):
    str +=f"{key} -> {value} \n"
print(str)
target = open('read_file2/source_file.hist.txt','wt')
target.write(str)
target.close()
       
