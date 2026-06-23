class Employee:
    salary  = 234
    increment = 20

    @property 
    def salaryandincrement(self):
        return (self.salary + self.salary * (self.increment)/100)

    @salaryandincrement.setter
    def salaryandincrement(self , salary):
        self.increment = ((salary/self.salary) - 1) *100


e = Employee()
e.salaryandincrement = 280.8
print(e.increment)