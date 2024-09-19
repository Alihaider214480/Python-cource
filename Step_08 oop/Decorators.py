#decorators enhance method functionanlity much more thing you can do using decorators it can take other method
#  and update them
# @staticmethod: For methods that don't need access to the class or instance.
# @classmethod: For methods that work with the class instead of instances.
# @property: Turns a method into a property, allowing it to be accessed like an attribute.
# @lru_cache: Caches function results to speed up repeated function calls.

class parents:
       
       income=0
       def __init__(self,growth,education) -> None:
           self.food=growth
           self.knowledge=education
       @staticmethod    
       def edu():
             return f"teach them to become best"
       @classmethod
       def grow(cls):
            return cls.income
       @property #This decorator allows you to turn a method into a read-only
       #property, meaning you can access it like a variable but calculate its value dynamically.
       def know(self):
             return f"{self.food}"
my_life=parents("education","love")     
print(my_life.know)      
print(parents.edu())#no need to make the instance of class or using object
print(parents.grow())