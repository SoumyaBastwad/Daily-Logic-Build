#counting the total number of vowels and consonents in given string
name=input("enter a string:")
vow=0
con=0
vowels=['a','e','i','o','u']
for i in name:
    if i in vowels:
       vow+=1
    else:
        con+=1
print("no of vowels:",vow)
print("no of consonents:",con)