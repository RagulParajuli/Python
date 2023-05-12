x = int(input("Enter your number:"))

match x:
    case _ if( x>0 and x%2==0) :
        print("It is even")
    case _ if( x>0 and x%2!=0) :
        print("It is odd")
    case _ if x==0:
        print("It is zero")
    case _:
        print("Try again")