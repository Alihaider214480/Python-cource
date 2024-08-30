name=input("what is your name?")
Name=list(name)
x=len(name)-1
reversed_string=""
vowels_count=0
vowels=set("aeiouAEIOU")
while x>=0:
    reversed_string+=Name[x]
    if Name[x] in vowels:
        vowels_count+=1
    x-=1
print(vowels_count)
print(reversed_string)