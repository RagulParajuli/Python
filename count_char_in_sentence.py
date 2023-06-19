sen = input("Enter your sentence:\n")
count = 0
for i in sen:
    if i == " ":
        continue
    else:
        count = count + 1
# count = len(sen)
print("No. of character:",count)

