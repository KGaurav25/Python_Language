print("Dictionary")
# Dictionary is list of key value pair

marks={
    "Shivani": 90,  # Key: "Shivani", Value: 90
    "Gaurav": 85,  
    "Mehuni": 78,
    92: "Sautan",   # Key: 92, Value: "Sautan"
}

empty_dict = {}  # Empty dictionary

print(marks, type(marks))
print(marks["Shivani"]) #use marks.get("Shivani")
# print(marks["Mehuni"])

print(marks.items())  
print(marks.keys())
print(marks.values())

# marks["Shivani"] = 95 #also update value

marks.update({"Shivani": 95, "YD": 25}) #update and add new key-value pair
print(marks)

print(marks.get("karan"))  #Returns None
# print(marks["karan"]) #Returns KeyError

marks.pop(92) #Remove key-value pair with key 92
print(marks)  

# marks.popitem() #Remove the last inserted
# marks.clear() #Clear all items in the dictionary 
# print(marks.items())   

print("\nSets")

s={1,2,3,4,5,5,5,5, "Sautan", }
print(s, type(s)) #elements are not repeated 
#set cannot conation dublicates

#s={} # It creates an empty dictionary, not a set
empty_set=set()  #Empty set
print(empty_set, type(empty_set))

s.add(6)
print(s)
s.remove(6)  
print(s)
print(len(s)) 
print(3 in s)  

print("\n")

s1={1,2,3,3,4,5}
s2={1,2,6,5,2,7,8}

print(s1.union(s2))
print(s1.intersection(s2)) 
print(s1.difference(s2))  # Elements in s1 but not in s2

print(s1-s2)  # Same as s1.difference(s2)