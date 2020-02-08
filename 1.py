"""a={"name":"mohit","id":20}
print(a)
print(a.values())

b='hi world'
c="hehe"
print(b+" "+c)

d=int(input("Enter"))
e=d/3
f=d//3
f+=3
print(e)
print(f)

g,f,h=2,5,1
if g>f and g>h:
    print(g)
elif f>g and f>h:
    print(f)
else:
    print(h)
n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*")
for i in [1,2,3,4,5]:
    if i==3:
        print ("Pass when value is",i)
    print (i)
a=['hi','ramu','mani','avi','rev']
for i in a:
    print(i,end="****")

a=[]
n=int(input("Enter"))
for i in range (0,n):
    a.append(input("item"))
for i in a:
    print(i,end=" ")


for i in range(0,10):
    print("%d*%d=%d"%(i,i,i*1))

n=int(input("n"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    n=n-1
    print(end="\n")
class classex:
    empcnt=0
    def __init__(self,ename,sal):
        self.ename = ename
        self.sal = sal
        classex.empcnt += 1


    def display(self):
        print("name:",self.ename,"salary:")

class manager(classex):
            def __init__(self,n,s):
                classex.init(self,n,s)

            employee1=classex("alek",1000)
            employee2=classex("sru",2000)
            employee2=classex("mohi",3000)
            employee2=classex("char",4000)
            employee1.display()
            print("total employees",classex.empcnt)

a=tuple(input())
print(a[-1])
print(a)
"""
class Employee:

   noOfEmployee = 0 # a data member to count the number of Employees

   totSalary = 0 # a data member to save the total salary

   # constructor for Employee class
   def __init__(self):
      self.name = input('Name :')
      self.family = input('Family :')
      self.department = input('Department :')
      self.salary = int(input('Salary :'))
      Employee.noOfEmployee += 1
      Employee.totSalary += self.salary

    #a function to return employee data
   def employeeDetails(self):
          employeeData = {}
          employeeData['Details of employee'] = Employee.noOfEmployee
          employeeData['Name'] = self.name
          employeeData['Family'] = self.family
          employeeData['Department'] = self.department
          employeeData['Salary'] = self.salary
          return employeeData

    #function to average salary
   def displayAvg(self):
        avg = Employee.totSalary/Employee.noOfEmployee
        return avg