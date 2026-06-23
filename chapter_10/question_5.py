from random import randint

class Train:

    def __init__(self , trainNo):
        self.trainNo = trainNo
    
    def book(self , fro , to):
        print(f"Ticket is booked in train NO. {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"train NO {self.trainNo} is running on time")

    def getfare(self , fro , to):
        print(f"Ticket is fare in train NO. {self.trainNo} from {fro} to {to} is {randint(22,333333)}")

t = Train(11233)

t.book("kakinada" , "Bengaluru")
t.getfare("Kakinda" , "Bengaluru")
t.getStatus()