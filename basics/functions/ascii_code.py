print ("Program has started!")
print ("Please enter a standard character: ")

character = input()

if len(character) == 1:
  x = ord(character)
  print(f"The ASCII code for {character} is {x}")

else:
  print("Wrong input, you should enter a single character. ")
print("Program ended!")