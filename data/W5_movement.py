
def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    path = movement ()
    #print(f"{path[0]} for {path[1]} steps")
    #print(f"{path[2]} for {path[3]} steps")
    for i in range(0, len(path), 2):
        print(f"{path[i]} for {path[i+1]} steps")

#range(start, end, step)
#range(end)
#range(start, end)

run()