contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice  = int(input("1.Add a new contact\n2.Search contact\n3.Display contact\n4.Edit Contact\n5.Delete contact\n6.Exit\nEnter your choice\n"))
    if choice == 1:
        name = input("Enter contact name")
        phone = input("Enter mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter contact name to search")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited")
        if edit_contact in contact:
            phone = input("Enter mobile number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n ?")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
