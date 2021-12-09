def search(name):
    print("Searching...")
    data = {}
    with open(name) as f:
        for line in f:
            if line.startswith("Section"):
                items = line.split(":")
                s_name = items[1].strip()
            elif s_name in data:
                data[s_name].append(line.strip())
            else:
                data[s_name] = [line.strip()]
    print("Done!")
    return data

def run ():
    d = search("data/files/txt/books.txt")
    #print(d)
    with open("data/files/txt/generated.csv", "w") as potato:
        for s, l_b in d.items():
            for item in l_b:
                potato.write(f"{s}, {item}\n")

run()