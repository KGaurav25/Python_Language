list=["Shivani", "Gaurav", "Khushi", 1, 2, False]

print(list)
print(list[0])
print(list[0:2])

list[0]="Khulii" #list are mutable
print(list)

list.append("Shivani")
print(list)

print("\n")
l1=[10, 80, 55, 46, 35, 76]
# l1.sort()
# l1.reverse()
# l1.insert(2,33) #insert 33 at index 2
# l1.pop(2) #remove element at index 2
# l1.remove(80) #remove 80 from list

print(l1.pop(2))
print(l1)

'''Lists are mutable Tuples are immutable'''
print("\nTuples")

tup=(1,2,3,4,"Shivani", "Gaurav", False, 3.14)
# a=(1,) #Tuple with one element
print(tup)
print(type(tup))

print(tup[5])
print(tup.count(4))
print(tup.index(3.14)) 
print(len(tup))

print(sum(tup[0:4]))
