"""
This program is to 
1. ask the user for Prof. Jekyll's file name;
2. read the file contents and counts the sum of the received points for each student;
3. print a simple (but sorted) report, just like this one:

"""

from os import strerror

sourcefile = input("Enter the source file name: ")

try:
    src = open(sourcefile,'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
dict = {}
line = src.readline().strip()
while len(line) > 0:
    for ch in line:
        if ch.isdigit():
            indx = line.find(ch)
            break
    name = line[:indx-1]
    name = " ".join(name.split())
    score = line[indx:]
    if name in dict.keys():
        dict[name] += float(score)
    else:
        dict[name] = float(score)
    line = src.readline().strip()
for key, value in dict.items():
    print(f"{key}     {value}")









        

        
            

            
        


       
    
    

    


        


