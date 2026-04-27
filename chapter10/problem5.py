from random import randint

class Train:

    def __init__(self, trainNO):
        self.trainNo = trainNO

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        print()

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
        print()

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
        print()


t = Train(12309)
t.book("Jaipur","Delhi")
t.getStatus()
t.getFare("Jaipur","Delhi")