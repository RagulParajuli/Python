def clas(class_atd, class_hld):
    per = (class_atd / class_hld)* 100
    if per>75:
        print("You can enter exam hall")
    else:
        m = input("Do you have medical certificate:")
        if m=='y':
            print("you are allowed")
        else:
            print("You are not allowed")

class_atd = int(input("Class Attended:\n"))
class_hld = int(input("Class held:\n"))
clas(class_atd, class_hld)

