print("Please enter a sequence: ")
seq = input()
print("Please enter the character for marker: ")
marker = input()

#if seq[] == 1:
    #count

m1 = 9999
m2 = 9999

#for letter in seq:
    #print(letter)

for pos in range(len(seq)): 
    #print(seq[pos])
    let = seq[pos]
    if let == marker:
        if m1 == 9999:
            m1 = pos
        #else:
            #m2 = pos
        elif m2 == 9999:
            m2 = pos

#print(f"Position 1: {m1}\nPosition 2: {m2}")

print(f"The distance between two markers is {m2-m1-1}")