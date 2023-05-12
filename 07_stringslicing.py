names="Hello! Ragul, It's me"
# slicing is used to print a string up to wherre user needed it
print(names[0:12]) 
# or
print(names[:12])
#string start to print from left side of slice and end with right side of the slice-1
print(names[14:21])
# or
print(names[14:])
print(len(names)) # len is used to find length of a string
print("names has",len(names),"letter words")
print("Full words")
print(names)
# or
print(names[:])
# -ve sign in slicing
print(names[0:-14])
# or
print(names[0:7])
# or
print(names[0:len(names)-14])
print(names[-21:-7]) # it means len-21 to len-7
