# Python program to demonstrate sorting by user’s choice

# Function to return the second element of the tuple
def sortSecond(val): 
    return val[1]

# List of tuples to demonstrate sorting
list1 = [(1, 2), (3, 3), (1, 1)]

# Sort list in ascending order by the second element
list1.sort(key=sorted)
print("Ascending by second element:", list1)

# Sort list in descending order by the second element
list1.sort(key=sorted, reverse=True)
print("Descending by second element:", list1)
