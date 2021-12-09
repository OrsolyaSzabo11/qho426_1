#initialise empty set
s = set()

#check the type is set
print(type(s))

#initialise non-empty set
colours = {"blue", "yellow", "red", "purple", "green"}

print(colours)

#adding elements to a set
colours.add("black")
colours.add("turquoise")


#Delete an element of a set
colours.remove("blue")

print(colours)

#Check membership
if "blue" not in colours:
    print("Yey, my favorite colour is here! ")
else:
    print("You are missing an important colour")


colors = {"yellow", "black", "red", "cyan"}

#Take union of two sets, join them together, but do not keep duplicates
print(colours.union(colors))

#Take intersection of two sets - the "common" elements
print(colours.intersection(colors))

#Take set difference - so only keep elements NOT in another collection
print(colours.difference(colors))
