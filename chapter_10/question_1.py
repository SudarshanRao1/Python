class Programmer:
    comapny = "Microsoft"

    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
suduru = Programmer("suduru" , 2000000 , 533004)

print(suduru.name , suduru.comapny , suduru.pin , suduru.salary)
