#asking user for name and if name is in alphabet then accept otherwise give a err message.
while True:
     name=input("enter your name?")
     if name.isalpha(): 
          break
     else :
         print ("name would be in alphabets plz try again")

#asking user for age and if age is in digit then accept otherwise give a err message.
while True :
    age=input("enter your age?")
    if age.isdigit():
        break
    else:
         print("Err age must be in digit try again.")

         
print(f"name:{name}")
print(f"age:{age}")

#Second method
"""
name=input("enter your name?")
age=input("enter your age?")
while True:
    if name.isalpha():
      break
    else :
        print("you must give alphbet")
while True:
    if age.isdigit():
        break
    else :
        print("your responce would be in digit")

print(name)
print(age)
"""