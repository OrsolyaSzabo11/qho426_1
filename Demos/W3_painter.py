#I want to create payment for a painter who's painting my house
def dimension():
  l = float(input("Enter length of the room: "))
  w = float(input("Enter width of the room: "))
  return l,w #returning a tuple of two values together

def calc_area(l, w):
    area = l*w
    return area

def name_room():
    return input("Enter the name of the room: ")

def price(name, area):
    if name.lower() == "bedroom":
        return 20*area
    elif name.lower() == "bathroom":
        return 12*area
    elif name.lower() == "kitchen":
        return 15*area
    else:
        return 55*area

def run():
    total_price = 0.0
    num = int(input("How many rooms would you like to paint? "))
    for i in range(num):
        n = name_room()
        length, width = dimension()
        area = calc_area(length, width)
        x = price(n, area)
        total_price += x
    print(f"The total cost of the job is: £{total_price}")

run()