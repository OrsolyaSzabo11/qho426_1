
#Initialise empty dictionary
phonebook = {}
d2 = dict()

#print(type(d1))

#Initialise non-empty dictionary
orsi_data = {"Name": "Orsi", "Age": 55, "Doggo": False, "Title": "Miss"}

#Print full dictionary
print(orsi_data)

#Use part of the dictionary for printing purposes
x = orsi_data["Name"]
y = orsi_data["Age"]
print(f"{x} is {y} years old")

#print({orsi_data["Name"]} is {str(orsi_data["Age"]} years old)

#Adding elements to the dictionary
phonebook["Max"] = "07482257335"
phonebook["Mark"] = "+5677467364736"
phonebook["Lucy"] = None

print(phonebook)

#Add more people to the phonebook
for i in range(3):
    n = input("Enter the name: ")
    numb = input(f"Enter {n}'s number: ")
    phonebook[n] = numb

name = input("Who would like to call? ")

if name in phonebook:
   print(f"Calling {name} with phone number {phonebook[name]}")
else:
  print(f"{name} is not your phonebook")
