# Write A Program To Create A String "We are studying Python" And Print All The Letters In The String Except y


x = "We are studying Python"

for i in x:
    if i == "y":
        continue
    else:
        print(i, end = "")
