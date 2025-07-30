# About the tuples in the Python
# Collection of items that are ordered and unchangable. Defined by enclosing items in the paranthesis(). Each item is seperated by comma.


# Key Characteristics:
# Ordered, Indexed, Immutable.

# Need Of tuple:
# Faster then list
# Fixed Collections
# Memory efficient

# Creating tuple
# With parenthesis
# a=(1, 2, 3, 4)

# Without Parenthesis
# a= 1, 2, 3, 4

# Single item tuple
# a=(a,) Comma is must required


a = (1, 2, 3, 4, ('A','B','C','D'),("Ram","Sita","Lakshmana","Hanuman"))

# Tuple Fun len()
print("The Length of the tuple is:",len(a))

# Tuple Fun count() number of times a specified number is present in the tuple
print("1 is present ",a.count(1),"Times in this tuple")

# Index fun index() first occurance of a specified item in tuple
print(a.index(3))

# Slicing the tuple
print(a[4:5])
print(a[5:6])


# Handaling the mixed data types in tuple

print(a[4])
print(a[4][2])
print(a[5])