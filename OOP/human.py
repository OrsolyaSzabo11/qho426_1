# class Human:

#   MAX_ENERGY = 100

#   def __init__(self):
#       self.name = "Human"
#       self.age = 0
#       self.energy = Human.MAX_ENERGY

#   def display(self):
#       print(f"I am {self.name}")

# if __name__ == "__main__":
#   human = Human()
#   human.display()

class Robot:

  MAX_ENERGY = 100

  def __init__(self):
      self.name = "Beep"
      self.age = 0
      self.energy = 0

  def __repr__(self):
      return f'Robot(name:{self.name}, age:{self.age}, energy:{self.energy})'

  def __str__(self):
      return f'Robot {self.name} is {self.age} years old.'


  def display(self):
      print(f"I am {self.name}")

  def grow{self}:
      self.age +=1
  
  def eat(self, amount):
      self.energy += amount
      if self.energy > Robot.MAX_ENERGY:
          self.energy = Robot.MAX_ENERGY

  def move(self, distance):
      self.energy -+ distance
      if self.energy , <0:
          self.energy = 0

if __name__ == "__main__":
  human = Robot()
  human.display()
  print(human)
  print(repr(human))
  human.move(83)
  human.eat(59)
  print(human)