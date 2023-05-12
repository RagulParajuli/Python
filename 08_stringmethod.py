a="Ragul ! @ #"
print(len(a))
print(a.upper()) # it convert 'a' string in uppercase
# existing strings are imutable 
print(a.lower())
# here original string is not changed but its duplicate is used for modification
print(a.rstrip("!@#")) # it only strip strings end part,  not begining part of string
print(a.replace("Ragul","Guess it")) # it replace Ragul by Guess it
print(a.split(" ")) # it places cuma where there is gap in string
b="i don't want To"
print(b.capitalize()) # it capitalize only first letter and it make others in lowercase
print(a.find("!"))
print(a.find("@"))
print(a.find("#"))

print(a.find("$"))   #find print -1 if a given input is not found
print(a.index("$")) #index print error if a give input is not found