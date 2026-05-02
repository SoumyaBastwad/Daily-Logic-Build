# cheaking whether the given number is palindrome or not by using while loop

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10          # Get last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove last digit

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
