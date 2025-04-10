student ={
    "name":"ranaMiah",
    "subject":{
        "math":56,
        "phy":76,
        "chem":66
    }
}
#return keys when keys no exist then return error
print(student.keys("name2"))

# return valus 
print(student.values())

# return key pairs
print(student.items())

# return value when keys no exist then return none
print(student.get("name"))

# update dict
print(student.update({"city":"dhaka"}))

