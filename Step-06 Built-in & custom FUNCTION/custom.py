#simple function
name=input("what is your name?")
def quote(name)->None:
    print(name)
quote(name)
#returning name ,age value
Name=input("name?")
Age=input("age?")
def Age_Name(Age:str,Name:str)->None:
    print(Age)
    print(Name)
Age_Name(Name,Age)
#returning type
def convert_farenheit_celcius(a)-> float:
   b=a/1.8-32
   return b
celcius_value=convert_farenheit_celcius(120)
print(celcius_value)