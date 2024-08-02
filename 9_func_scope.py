#x = 10
#def func():
  #  x =int(input("enter the number: "))
 #   return x
#print(func())
#print(x)


x = 10
def func():
    global x
    x =50
    return x
print(x)
print(func())
print(x)

