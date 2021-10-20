'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if{self.seats>0}:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        self.seatNo = seatNo
        s2 = set(self.seatNo)
        s2
        s1 = set[self.seats]
        s1.add(self.seats)
        print(f"Your ticket has been cancelled!")
        
    def getStatus2(self):
        print("************")
        print(f"Now seats available in the train are {self.seats}")
        print("************")

intercity = Train("Intercity Express: 14015", 90, 5)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket(5)
intercity.getStatus2()
