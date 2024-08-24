name=input("plz enter your string/number to reverse\n")
Name=list(name)
x=len(name)
x-=1
while x>=0:
     print(name[x],end="")
     x-=1





#second method
"""
name=input("plz enter your string/number to reverse\n")
Name=list(name)
for x in range(len(name)-1,-1,-1):
    print(Name[x],end="")
"""
