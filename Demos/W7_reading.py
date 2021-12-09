import csv
def writing_csv():
    with open("d.csv", "w") as data:
        #csv_writer = csv.writer(data, delimiter = "@")
        csv_writer = csv.writer(data)
        for i in range (3):
            print("Enter the name")
            n = input()
            print("Enter the age")
            a = input()
            print("Enter the favorite album")
            album = input()
            csv_writer.writerow(list((n, a, album)))
        
def reading_csv():
    with open("d.csv") as bob:
        csv_reader = csv.reader(bob)
        #print(csv_reader)
        for line in csv_reader:
            print()
            for item in line:
                print(item, end = ",")

reading_csv()