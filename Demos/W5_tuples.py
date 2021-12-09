def simple_tuples():
    person = ("Orsi", 67, False)

    #Printing a tuple
    print(person)
    #check data type
    print(type(person))
    #access elements via IndexvError
    print(f"{person[0]} is {person[1]} years old")
    #no mutation possible
    #person[0] = "Orsi"
    #print(person)
    if person[2]:
        print("You have a doggo!")
    else:
        print("No doggo no fun!")
#tuples can be concanated (joined) - but this creates a different tuple
p1 = person + (20, "NotImplemented")
print(p1)
print(person)
t = (16, 8, 9, 21, 55)
print(max(t))
print(min(t))
print(min(p1))

simple_tuples()