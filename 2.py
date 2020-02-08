class Emp():

    Count = 0
    Sum=0
    Avg =0

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        Emp.Count += 1
        Emp.Sum += self.salary

    def displayEmp(self):
        print("id : ", self.id, ", Name : ", self.name, ", Salary: ", self.salary, ", department: ", self.department)


class FullTimeEmp(Emp):
    def __init__(self, id, name, salary, department):
        Emp.__init__(self, id, name, salary, department)


employ1 = Emp(1, "Ramu", 100000, "Ece")
employ2 = Emp(2, "Mohit", 8000, "Cse")
employ3=FullTimeEmp(3, "Sri", 7000,"It")
employ4=FullTimeEmp(4,"Ram",9000,"cse")

print("Total Employees %d" % Emp.Count)
print("Average salary of the employees is", (Emp.Sum/Emp.Count))
print(employ1.displayEmp())
print(employ2.displayEmp())
print(employ3.displayEmp())