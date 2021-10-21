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
            y = self.seats - 1
            print(f"Your ticket has been booked! Your seat number is {y}")
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        self.seatNo = seatNo
        l = [self.seats]
        i = 1
        while i < self.seats:
            l.append(i)
            i = i + 1
            break
        l.sort()
        l.append(self.seatNo)
        j = 0
        while j < self.seats:
            l.pop(j)
            j = j + 1
            break
        l.remove(self.seats)
        strings = [str(l) for l in l]
        a_string = "".join(strings)
        an_l = int(a_string)

        print("************")
        print(f"Now seats available in the train are {an_l}")
        print("************")

intercity = Train("Intercity Express: 14015", 90, 5)
intercity.getStatus() 
intercity.bookTicket()
intercity.cancelTicket(5)

