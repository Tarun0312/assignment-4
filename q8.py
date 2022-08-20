# 8. Write a python script to calculate simple interest

principal=int(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
year=float(input("Enter the value for how many years u have taken this amount: "))
SI=(principal*rate*year)/100
print("The Simple Interest is",SI)