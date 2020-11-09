# Write A Program To Create A String "We are studying Python" and Remove Vowels Form The String


x = "We are studying Python"
y = "aeiou"

for i in x:
    if i not in y:
        print(i, end = "")
