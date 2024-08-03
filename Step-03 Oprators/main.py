# Arithmetic Operators: Used to perform basic mathematical operations.
""""
a=int(input("enter your 1st number"))
b=int(input("enter your 2nd number"))
# + (Addition)
print(a+b)
# - (Subtraction)
print(a-b)
# * (Multiplication)
print(a*b)
# / (Division)
print(a/b)
# % (Modulus)
print(a%b)
# ** (Exponentiation)
print(a**b)
# // (Floor Division)
print(a//b)
# Assignment Operators
# +=
# -=
# *=
# /=
# //=
# %=
# **=
# """
""""
c = 5
print(c)
c += 2  # equivalent to c = c + 2
print(c)
c = 5
c -= 2  # equivalent to c = c - 2
print(c)
c = 5
c *= 2  # equivalent to c = c * 2
print(c)
c = 5
c /= 2  # equivalent to c = c / 2
print(c)
c = 5
c //= 2  # equivalent to c = c // 2
print(c)
c = 5
c %= 2  # equivalent to c = c % 2
print(c)
c = 5
c **= 2  # equivalent to c = c ** 2
print(c)
"""
# ? Comparison Operators
"""
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
"""
"""
c=int(input("enter the first number"))# c=4
d=int(input("enter the second number"))# d=8
print(c==d) #false
print(c!=d)# true
print(c>d)# false
print(c<d)#true  
print(c>=d)#false
print(c<=d)#true
"""
#Logical Operators
""""
there are three logical Oprators
AND
or
not
"""
e=int(input("enter your value of e"))#e=12
f=int(input("enter your value of f"))#f=10
print(e>f and e==f)#false
#and only true if both statement true
print(e>f or e==f)#true
# or false only when both statment false
print(not(e>f and e==f))#true
#it will give opposite 
"""
Identity Operators
is
is not
"""
h = 5
i = 6
j = 5
print(h is i)  # False (h and i are not the same)
print(h is j)  # True (h and j are the same)
print(h is not i)  # True (h and i are not the same)