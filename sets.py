# About the sets in python and various details about it.

# Ways to create set in python
s1 ={'A','B','C','D','E','F'}
s2=set([1,2,3,4,5,6])

# Adding elemtnts to the set
s1.add(55)
s2.update([119,33023,334])
print(s1)
print(s2)

# Removing the elements from a set 
s1.discard('A')
print(s1)

# If you remove an item which is not present in the set then this will thow the error
s1.remove('B')
print(s1)

# This will make the set empty
s1.clear()
print(s1)

# del will delete the set and its existance and if you try to access it will generate error
del s1
# print(s1)


# Other sets operatoins
print(len(s2))  # To print the number of items present in the set
print(6 in s2) # To know if the set contain the item in it
print(100 in s2) 

# Set operations : Union, Intersection, Difference

p1=set(["apple","ball","cat","dog","elephant","fish","garden","orange"])
p2=set(["orange","olive","oman","okhati"])

print(p1|p2) #For the Union (every unique items)
print(p1&p2) #For the intersection (common items only)
print(p1-p2) #Returns the items present in first set but not in the second
print(p1^p2) #Returns the items which are unique in the both sets



# The various subset and superset operations are isdisjoint(),<=,>=,<,>
h1={1,2,3,4,5,6,7}
h2={2,4,6,8,10}

print(h1.isdisjoint (h2))
print(h1<=h2)
print(h1<h2)
print(h1>=h2)
print(h1>h2)