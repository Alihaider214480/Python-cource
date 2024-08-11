# simple if else statements
age=int(input("what is your age?"))

""""
if age<18:
    print("you are not adult")
else :
     print("you are adult")
     """
#nested if else statement
""""
if age>=18:
    if age>60:
        print("you are now old enough to have a retirement")
    else :
        print("you have to work hard and smart to get success")
else :
    print("be prepare for future")
    """
#if elif statement
""""
if age<=18 :
       print("your parents are your responsible")
elif age==18:
       print("now you have to take control of your future")
elif age>18 :
       print("now you have to quite all bad habit start life with goal")
elif age>60:
       print("live your life with your closer one")
else :
       print("rip")
       """
#match-case (switch) statements,
match age:
    case 12:
         print("your parents are your responsible")
    case 18:
          print("now you have to take control of your future")
    case 60:
          print("live your life with your closer one")
#match case using if statement
match age:
    case _ if age>12 and age<18:
               print("your parents are your responsible")
    case  _ if age>18 and age<45:
               print("now you have to take control of your future")
    case  _ if age>60:
               print("live your life with your closer one")