
import matplotlib.pyplot as plt

with open("visual/subplots/temps.txt") as t:
      lista = t.readlines()
      listb = []
      for item in lista:
          listb.append(int(item.strip("\n")))

print(listb)
