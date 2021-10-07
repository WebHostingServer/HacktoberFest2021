import csv

def create_mobile():
    name = str(input("Enter mobile contact:"))
    mobile = str(input("Enter mobile number:"))
    headers = ['name', 'mobile']
    with open("mobile.csv", "a+", encoding='UTF8', newline='') as f:
        writer  = csv.DictWriter(f,fieldnames=headers)
        writer.writerow({'name':name, 'mobile':mobile})

def read_mobile():
    headers = ['name', 'mobile']
    with open("mobile.csv", "r+", encoding='UTF8') as f:
        reader = csv.DictReader(f,fieldnames=headers)
        print("Row\tName\t\tMobile")
        print("-" * 30)
        row_index = 1
        for line in reader:
            print(row_index, "\t", line['name'],"\t\t",line["mobile"])
            row_index = row_index + 1

def display_menu():
    print("-" * 30)
    print("1. Create a new mobile number on CSV")
    print("2. Read all mobile numbers from CSV")
    print("0. Exit")
    menu = int(input("Enter you menu number [0,1,2]:"))
    print("-" * 30)
    return menu

menu = display_menu()

while menu != 0:
    if menu == 1:
        create_mobile()
    elif menu == 2:
        read_mobile()
    elif menu == 0:
        exit
    menu = display_menu()