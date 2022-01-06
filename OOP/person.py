#The class Person will be a blueprint / template for any objects to store information about humans
class Person:

  #Class attribute - > constant, which is visible to all objects of the class
    MAX_ENERGY = 100

  #Static method -> Utility function, which does not require an objevt to exist

  def is_mature(age):
      if age >= 35:
          return True
      else: 
          return False

  #Initianiliser/Constructor -> function that is invoked / used immediately when the object is created
    def __init__(self, name = "", age = 1, job = "None", weight = 5, energy = 100):
        #These will be instance attributes (features of each object)
      self.name = name
      self.age = age
      self.job = job
      self.weight = weight
      #self.energy = energy
      if energy > Person.MAX_ENERGY:
        self.energy = Person.MAX_ENERGY
      else:
        self.energy = energy

    #"Dunder" = Double Underscore
    #Magic Method __str__ which is invoked by print function automatically
    def__str__(self):
        return f"Name:{self.name} Age:{self.age} Job:{self.job} Weight: {se;f.job} Energy:{se;f.energy}"

    #Instance method that works on eeach object of the class
    def hello(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old. I work as {self.job}. I weigh {self.weight}. My energy is currently {self.energy}. Nice to meet you. ")

    def grow(self, years):
        self.age += years

    def eat(self, food, w = 0.5):
        print(f"{self.name} have eaten {food}. ")
        self.weight += w
        print(f"They now weight {self.weight}kg")

p1 = Person("Alessandro", 28, "MacGyver", 68, 99)
p2 = Person("Dawid", 22, job = "Clerk")
p2.hello()
#p2.Hello()
#p2.Hello()

print(p1)
print(p2) hello()
p1.hello()
print(f"{Person.is_mature(50)}")
print(f"{Person.is_mature(22)}")
print(f"{Person.is_mature(p2.age)}")

#p1.weight += 17
#p2 = Person("Dawid", job = "Clerk")
#print(f"The new person is called {p1.name}. They are {p1.age} years old and weight {p1.weight} kg. They work as {p1.job}")
#print(f"The new person is called {p2.name}. They are {p2.age} years old and weight {p2.weight} kg. They work as {p2.job}")