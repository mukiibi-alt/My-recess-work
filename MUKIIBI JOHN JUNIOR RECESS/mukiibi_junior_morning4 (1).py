# Assignment: Show encapsulation with employee information to give a pay increment (salary with employee information to  new_salary)
#e.g from 850000 to 1000000
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def display_olddetails(self):
        print("Name: ", self.__name)
        print("Salary: ", self.__salary)
    def display_newdetails(self):
        if self.__salary > 200000:
            self.__salary = self.__salary + (self.__salary * (15/100))
        else:
            self.__salary = self.__salary + (self.__salary * (20/100))
        print(f"{self.__name}, your salary has been increased to {self.__salary}")
emp = Employee("Jnr", 300000)
emp.display_olddetails()
emp.display_newdetails()
emp2 = Employee("Mukiibi", 150000)
emp2.display_olddetails()
emp2.display_newdetails()






