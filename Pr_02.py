import math

class Calculator:
    def __init__(self,num):
        self.number = num
    
    def option(self):
        print(f"Options are: \n","(1) Square\n","(2) Cube\n","(3) Sqrt\n")
        x =  input("Enter a option: ")

        if x == "1" or "Square":
            print(f"The Square of the given number is: {int(self.number**2)}") 
        elif x == "2" or "Cube":
            print(f"The Cube of the given number is: {int(self.number**3)}")     
        elif x == "3" or "Sqrt":
            print(f"The Sqrt of the given number is: {math.sqrt(self.number)}") 
    @staticmethod
    def greet():
        print("Hello")


a = Calculator(int(input("Enter a number: ")))
a.greet()
a.option()



    
