def observed():
  observations = []
  for i in range(5):
    inp = input("Enter new value: ")
    observations.append(inp)
  return observations

#print(observed()) this is how I run the function

def remove_observation(x = []):

  while True:
    print("Please enter an observation to be removed: ")
    obs = input()
    if obs in x:
        x.remove(obs)
    print("Would you like to remove an observation? ")
    response = input()
    if response != "yes":
        break
  #return x

#print(remove_observation(observed()))

#this is the first function 

def run():
    lista = observed()
    remove_observation(lista)
    obs_set = set()
    for i in lista:
        tuplex = (i, lista.count(i))
        obs_set.add(tuplex)
    #return(obs_set)
    print("Observations:")
    for thing in obs_set:
        print(f"{thing[0]} has been observed {thing[1]} times")

#print(run())
run()
