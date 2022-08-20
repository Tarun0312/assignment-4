# 3. Write a python script which takes two numbers from the user, then calculate their sum
# and display the result.

x=int(input("Enter first number: "))
# input function returns string but we've to add two integers so use int() function to convert str into int
y=int(input("Enter second number: "))
z=x+y
print("Sum is",z)