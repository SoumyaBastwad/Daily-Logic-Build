# finding the factorial of the given number

num=int(input("enter a integer: "))
fact=1
a=1
while a<=num:
    fact=fact*a
    a+=1
print("the factorial of ",num,"is",fact)
