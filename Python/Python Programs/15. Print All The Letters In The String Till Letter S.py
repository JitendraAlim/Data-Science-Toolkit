# Write A Program To Create A String "We are studying Python" And Print All The Letters In The String Till Letter s


x = "We are studying Python"

for i in x:
    if i == "t":
        break
    else:
        print(i, end = "")
