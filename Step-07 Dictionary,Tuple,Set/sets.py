# ? A set is an ordered collection of unique elements
my_set={12,23,"pak","india"}
print(my_set)
#there is no order in out put so you have to give a unique values if you give duplicate values 
# it automatically remove them

new_set={12,15,12,"play","ball","play"}
print(new_set)#{'ball', 12, 15, 'play'}

#beacause it muteable so you update it using add or remove
new_set.add("bat")
print(new_set)#output {'play', 12, 15, 'ball', 'bat'}
new_set.remove("bat")
print(new_set)#output {'ball', 12, 15, 'play'}
#you can check a elemnt presence by in method
check_ele="play" in new_set
print(check_ele)
#you can check set operations by union"|",intersection "&",difference "-"
union_set=my_set | new_set
print(union_set)#{'play', 12, 15, 'pak', 23, 'india', 'ball'}
intersection_set=my_set & new_set
print(intersection_set)#{12}
set_difference=my_set - new_set
print(set_difference)#{'india', 'pak', 23}