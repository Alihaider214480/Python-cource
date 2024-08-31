# ? A tuple is an immutable, ordered collection of elements.
tuple=(12,34,"hello",1.3,"Pakistan")
print(tuple)
#you can access tuple elemnts by index
print(tuple[4]) 
# it can contain dublicate elements
dup_tuple=(1,1,1,2,3,4,5,32,2,1,3,4)
#you can use count method to calculate how many time a element is repeated
print(dup_tuple.count(1))#output 4
print(dup_tuple.count(2))#output 2
print(dup_tuple.count(3))#output 2