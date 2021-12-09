# f = open("computing.txt", "a")

# x = input("Sing me a song: ")
# f.write(x)
# f.write("\n")

# lista = ["Alessandro", "Dawid", "Wesley", "Fikret", "Orsula"]
# for i in range(len(lista)):
#   f.writelines(lista[i]+"\n")

f = open("computing.txt")
print(f"\033[96m{f.read()}\033[0m")

f.close()