import math

class sum:
    def sum(self):
       num1 = int(input("Enter a number: "))
       num2 = int(input("Enter a number: ")) 
       print(f"Sum of the given numbers is: {num1+num2}")

x = sum()
x.sum()

class ma(sum):
    def ma(self):
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))
        print(f"Sum of the given numbers is: {num1*num2}")

x = ma()
x.ma()        
