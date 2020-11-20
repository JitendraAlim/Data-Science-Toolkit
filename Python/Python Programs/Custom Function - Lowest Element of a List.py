# Write a function that receives a list, and returns the lowest element of the list.

def lowest(list):

    # Initial minimum value
    min = list[0]

    # We check every element in the list
    for i in list:

        # If the selected element is less than previous element
        if i < min:

            # Update the initial minimum with the selected element
            min = i

    # Returning the minimum element from the list.
    return min


# Using the function on a list.
print(lowest([3,5,1,7,9]))
