name="Ragul"
sent="It's me"
# or
Sent='Let me show you a sayari'
print("Hello, "+name)
print(sent)
print(Sent)
'''  triple (') is used to print multiple line string if it is stored in variable
or usedc to store mutiple line comment if not store in variable'''
sayari='''बिन तुम्हारे तो सिर्फ साँसें चलती है
ज़िंदगी तो वो होती है जिसमें तुम साथ होते हो'''
print("\n",sayari,"\n")
# printing string letter by letter
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("Let's use for loop to print string\n")
for character in sayari:
      print(character)