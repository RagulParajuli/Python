n = int(input("Enter your number:\n"))
a = 0
b = 1
print(a)
print(b)
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)