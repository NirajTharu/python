# About the Modifying the list
# List in python is mutalbe  which means the content inside the list can be modified after they are created

a=[1, 2, 3, 4, 5, 6, 7, 7]

# append(): for adding an item to end of the list || this modifies the list  does't create a new one
a.append(99) 
print(a)

# insert():for addition of item to the desired place, where first input is for the place and second is for the item
a.insert(3,7)
print(a) # output: [1, 2, 3, 7, 4, 5, 6, 7, 7, 99]

# For checking an item is present in the list or not will return True when present else False
print(34 in a) #output: False

# count(): for the number of times item  appears in the list
print(a.count(4)) #output:1
print(a.count(7)) #output:3

#index():return the first occurance of item in the list
print(a.index(7))
print(a.index(99))

#Removing items 
# By value:
a.remove(7) 
print(a) #output:[1, 2, 3, 4, 5, 6, 7, 7, 99]

# By index:
print(a.pop()) #remove the last value of the list
print(a) # output: 99
print(a.pop(3)) #output: 4
print(a) #output: [1, 2, 3, 5, 6, 7, 7]


# General List Functions
print(max(a))
print(min(a))
print(sum(a))

# For reversing the list
a.reverse()
print(a) #[7, 7, 6, 5, 3, 2, 1]

# For sorting a list
a.sort()
print(a) #output:[1, 2, 3, 5, 6, 7, 7]
