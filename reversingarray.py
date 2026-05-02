#write a program to reverse the order of element in array
# sample input:[1,2,3,4,5]

arr=[1,2,3,4,5]
print(arr[::-1])

#another way
arr=[1,2,3,4,5]
rev=[]
for i in arr:
    rev=[i]+rev
print(rev)

#by using appending method
arr=[1,2,3,4,5]
rev=[]
for i in range(len(arr)-1,-1,-1):
      rev.append(arr[i])
print(rev)
