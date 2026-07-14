# Simple Contact Book(Task 5)
contacts = {}
while True:
    c = input("1:Add 2:View 3:Search 4:Delete 5:Exit : ")
    if c == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts[name] = [phone, email]
    elif c == "2":
        print(contacts)
    elif c == "3":
        print(contacts.get(input("Name: "), "Not Found"))
    elif c == "4":
        contacts.pop(input("Name: "), None)
    elif c == "5":
        break