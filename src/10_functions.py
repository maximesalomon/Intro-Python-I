# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


##################################

numlst = [7, 13, 68, 23, 9, 186]

def centered_average(lst):
    lst.sort()
    return sum(lst[1:-1]) / (len(lst) - 2)

print(centered_average(numlst))