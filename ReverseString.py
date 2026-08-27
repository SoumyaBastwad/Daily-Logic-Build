#by taking the input from the user as string and that string revesing
string=input("Enter a string:")
rev=''
for i in string:
    rev=i+rev
print(rev)

# reversimg string by using slicing metod and creating function for that
string=input("Enter a string:")
def RrversingString(string):
   print(string[::-1])

RrversingString(string)
