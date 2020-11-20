# Write a function that receives a list and a number x. You must return the position of the first element that is divisible by x.

def first_divisible(list, x):

    # Iterating over all elements of the list
    for i in range(len(list)):

        # If the i'th element of the list is divisible by x
        if (list[i] % x == 0):

            # Then (i+1)th element is the first element of the list that's divisible by x.
            return i + 1
        else:

            # If the i'th element of the list is not divisible by x, then check the next element.
            continue


# Using the function
print(first_divisible([1,2,4,5,6],3))
