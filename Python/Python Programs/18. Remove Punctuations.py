# Write A Program To Remove Punctuations From The String "Hello!!!,(How are you...?).Good Morning"


x = "Hello!!!,(How are you...?).Good Morning"
y = "!,?."

for i in x:
    if i not in y:
        print(i, end = "")
        
        
