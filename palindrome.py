"""

palindrome: It's a word which look the same when read forward and backward.
For example, "kayak" is a palindrome, while "loyal" is not.

Assume that an empty string isn't a palindrome;
Treat upper- and lower-case letters as equal;
Spaces are not taken into account during the check - treat them as non-existent;

"""
text = input("Please enter a text: ").lower()
#text = ''.join(text.split())
text = text.replace(" ","")
#print(text)
if len(text) != 0:
    for i in range(len(text)):
        if text[i] != text[-(i+1)]:
            print("It's not a palindrome")
            quit()
    print("It's a palindrome")
else:
    print("It's not a palindrome")

