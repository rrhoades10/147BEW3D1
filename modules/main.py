# driver code will live in main.py 
# hub for all the other code to join in and mingle
import modules.contact_manager as contact_manager
# we could also name each function 
# from contact_manager import add_contact, delete_contacts, search_contacts, view_contacts

# we could also apply aliases to any of our custom functions as well

def main(): #generally the naming convention for the function running your program
    contacts = [] #contacts list we're using as an argument for all our functions   

    while True:
        print("\n1. Add Contact \n2. View Contacts \n3. Search Contact \n4. Delete Contact \n5. Quit")
        choice = input("Choose an Option: ")
        if choice == "1":
            name = input("Enter a name: ")
            phone = input("Enter phone number: ")
            email = input("Enter Email: ")
            contact_manager.add_contact(contacts, name, phone, email)

        elif choice == "2":
            contact_manager.view_contacts(contacts)

        elif choice == "3":
            name = input("Enter a name to search: ")
            contact = contact_manager.search_contacts(contacts, name)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print("Not found")

        elif choice == "4":
            name = input("Enter name to delete: ")
            deleted_contact = contact_manager.delete_contacts(contacts, name)
            if deleted_contact is not None:
                print(f"Contact successfully deleted: {deleted_contact}")
            else:
                print("Contact Not Found")

        elif choice == "5":
            break

        else:
            print("Please enter a valid input! ")

# when using imports we check that the function we're calling is in the current file
if __name__ == "__main__":  
    print(__name__) 
    main()






