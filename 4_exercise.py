user1=int(input("enter first number"))
user2=int(input("enter second number"))
def greater_number(a,b):
    if a>b:
        return a
    return b
bigger= greater_number(user1,user2)
print(f"{bigger} is greater")   
