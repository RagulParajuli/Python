def fact(n):
    # for i in range(n):
     if(n==1):
      return(n)
     else:
        return(n*fact(n-1))

x = int(input("Enter your number:\n"))
# print(fact(x))
fact = fact(x)
print("The factorial of",x,"is",fact)
