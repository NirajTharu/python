# About the type() function in python to detect the data type of a variable or a value

a= 16 #ouptu:<class 'int'>
print(type(16))

b= "python" #ouptu:<class 'str'>
print(type("python"))

c= a + 4j #ouptu:<class 'complex'>
print(type(c))

e=None
print(type(e)) #ouptu:<class 'None'>

f=[1,2,3,4, 5]
print(type(f)) #Dynamic array that can hold the multiple items

g=(22,33,44,55)
print(type(g)) #immutable sequence

h={0,9,8,7,6,5,4,3,2}
print(type(h)) #Unordered collection of unique items

i={a:"apple",b:"ball",c:"cat"}
print(type(i)) #Dictonaries store the key value pairs