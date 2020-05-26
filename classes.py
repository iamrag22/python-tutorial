# Simple classes
class Vehicle:
    def __init__(self, license_id, color):
        self.id = license_id
        self.color = color
    
# Inheritance
class Car(Vehicle):
    def __init__(self, license_id, color, manufacturer):
        super().__init__(license_id, color)
        self.manufacturer = manufacturer


car1 = Car("123","black", "honda")
car2 = Car("456","blue", "toyota")

print(car1.color, car1.manufacturer,car1.id)
print(car2.color, car2.manufacturer,car2.id)

# Attributes are public by default
# Use properties to access in a clean/datahiding fashion

class Person:
    count=0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count+=1
    
    @property # For Get
    def name(self):
        return self.__name
    
    @name.setter # name should be the property name
    def name(self, some_other_name):
        self.__name = some_other_name
    
    @property
    def age(self):
        return self.__age

    @classmethod
    # cls is key word
    def get_instances_count(cls):
        return cls.count
    
    @staticmethod
    def print_this_for_all_objects():
        print("Python is awesome")


# Instance Methods and properties
p = Person("Foo", 50)
print(p.name,p.age)
p.name = "Bar" # valid
print(p.name,p.age)

# p.age = 20  # Not valid as age is read only
p.__name = "fgg" # No effect
p.__age = 35 # No effect

# Class methods
print(Person.get_instances_count())

# static methods
Person.print_this_for_all_objects()

# Composition
class Laptop:
    def __init__(self, model, cpu, gpu):
        self.model = model
        # Composition
        self.cpu = cpu
        self.gpu=gpu
    
    def get_description(self):
        print(self.model, self.cpu.name, self.gpu.name)

class CPU:
    def __init__(self, name):
        self.name = name

class GPU:
    def __init__(self, name):
        self.name = name

laptop = Laptop("Dell", CPU("Intel"), GPU("Nvdia"))
laptop.get_description()
print(type(laptop) is Laptop) # Type check

