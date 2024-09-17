#simple class programme
class Car:
    wheel=4
    @staticmethod
    def add(a,b):
       return a+b
    
    def __init__(self,userbrand,usermodel):
     self.brand=userbrand
     self.model=usermodel

    @classmethod
    def price(cls,tyre):
       cls.wheel += tyre
       return cls.wheel
    def full_name(self):
       return f"{self.brand} {self.model} have {self.wheel} wheel"
    
    
my_car=Car("toyata","corolla")
print(my_car.brand)
print(my_car.wheel)
print(my_car.full_name())

print(Car.add(12,23))
print(Car.price(10))