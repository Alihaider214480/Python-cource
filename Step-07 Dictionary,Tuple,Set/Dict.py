# ? A dictionary is an    ordered, mutable collection of key-value pairs.
#in python every thing we write is an object
Bio_data={"name":"Ali","age":25,"educaation":"FSC,DAE"}
print(Bio_data)
#we can access key_value pair by entering the key
print(Bio_data["name"])
#we can update any value using key
Bio_data["age"]=26
#we add any other key value pair also
Bio_data["Father"]="RAJAB ALI"
print(Bio_data)
#we delete any key
del Bio_data["educaation"]
print(Bio_data)
#pop method also use to delete but it return pop out value
age=Bio_data.pop("age")
print(age)
print(Bio_data)
#you can check the items using "in" or "not in"
if "age" in Bio_data:
    print("its in bio data")
else:
    print("plz try with another keyword")
#not in convert false to true and true to false
if "age" not in Bio_data:
    print("its in bio data")
else:
    print("plz try with another keyword")

#we can itrate over keys , value and on key value pairs
#itrate over key
for key in Bio_data:
    print(key)
#itrate over values
for value in Bio_data.values():
    print(value)
#itrate over both key,values pair
for key,value in Bio_data.items():
    print(f"{key},{value}")
#in dictionary no dublicate key,key must be unique otherwise it remove dublicate key
unique_keys={"place":"islamabad","place":"pakistan"}
print(unique_keys)#output shows place pakistan only
# Using Dictionary Methods

# ? Dictionaries come with several useful methods, such as get(), keys(), values(), items(), and clear().

# ? get(): Returns the value for a key, or None (or a specified default value) if the key is not found.
print(Bio_data.get("name"))  # Output: ALi
print(Bio_data.get("city"))  # Output: Not Found

# ? keys(): Returns a view object containing the dictionary's keys.
print(Bio_data.keys())  # Output: dict_keys(['name', 'FATHER'])
# ? values(): Returns a view object containing the dictionary's values.
print(Bio_data.values())  # Output: dict_values(['Ali', "RAJAB ALI"])
# ? items(): Returns a view object containing the dictionary's key-value pairs.
print(Bio_data.items())  # Output: dict_items([('name', 'Ali'), ('Father', "RAJAB ALI")])
# ? clear(): Removes all key-value pairs from the dictionary.
Bio_data.clear()
print(Bio_data)  # Output: {}