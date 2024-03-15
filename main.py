# task_1
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"{self.num1 + self.num2}"

    def subtract(self, ):
        return f"{self.num1 - self.num2}"

    def multiply(self):
        return f"{self.num1 * self.num2}"

    def divide(self):
        return f"{self.num1 / self.num2}"

obj = Calculator(10, 2,)
obj1 = Calculator(10, 2)
obj2 = Calculator(10, 2)
obj3 = Calculator(10, 2)

print(obj.add())
print(obj1.subtract())
print(obj2.multiply())
print(obj3.divide())



# task_2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            return f"{other.name} is older than me."

        elif self.age > other.age:
            return f"{other.name} is younger than me."

        elif self.age == other.age:
            return f"{other.name} is the same age as {self.name}"



p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))

print(p2.compare_age(p1))

print(p1.compare_age(p3))




# Task_3
inp = input("enter about football player: ")

class Football_player:


    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


    def get_name_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"



ply = Football_player("Kevin De Bruyne", 32, 181, 70)
print(ply.get_name_age())
print(ply.get_height())
print(ply.get_weight())



#Task_4
inp = input("enter add or subtract or multiply or divide:")
result_for_add = 0
result_for_subtract = 0
result_for_multiply = 1
result_for_divide = 1
string = "10", "5"
for num in string:
    intgr = int(num)
    if inp == "add":
        result_for_add += intgr
        print(result_for_add)
    elif inp == "subtract":
        result_for_subtract -= intgr
        print(result_for_subtract)
    elif inp == "multiply":
        result_for_multiply *= intgr
        print(result_for_multiply)
    elif inp == "divide":
        result_for_divide /= intgr
        print(result_for_divide)
    else:
        print("it isn't maths")


#Task_5
inp = input("enter employee: ")
class Person:
    def __init__(self, name, username, inp):
        self.name = name
        self.username = username
        self.input = inp

    def fullname(self):
        return f"{self.name} {self.username}"

    def email(self):
        return f"{self.name}.{self.username}@company.com"

    def firstname(self):
        return f"{self.name}"



obj = Person("Della", "Smith", inp=inp)
if inp == "fullname":
    print(obj.fullname())

elif inp == "email":
    print(obj.email())

elif inp == "firstname":
    print(obj.firstname())


#Task_6
inp = input("enter name: ")
class Person:
    def __init__(self, f_name, l_name, fullname, initials, inp):
        self.f_name = f_name
        self.l_name = l_name
        self.fullname = fullname
        self.initials = initials
        self.input = inp

    def first_name(self):
        return f"{self.f_name}"

    def last_name(self):
        return f"{self.l_name}"

    def full_name(self):
        return f"{self.f_name} {self.l_name}"

    def short_forms(self):
        return f"{self.initials}"


obj = Person("Della", "Smith", "Della Smith", "D.S", inp=inp)
if inp == "fname":
    print(obj.f_name())

elif inp == "lname":
    print(obj.l_name())

elif inp == "fullname":
    print(obj.fullname())

elif inp == "initials":
    print(obj.initials())

else:
    print("error")



