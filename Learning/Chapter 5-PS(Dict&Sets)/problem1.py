dic={
    "Hi": "Namskar",
    "Bye":"Yeto",
    "How are you?":"kas ahes?",
    "name":"Nav",
    "Yes":"Vhay"

}

print(dic.items())  

a=input("Enter a word: ")

print(dic.get(a, "choice not found"))
