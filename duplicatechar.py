#program to remove duplicate character
name=input("enter a string:")
newname=" "
for i in name:
    if i not in newname:
        newname+=i
print(newname)