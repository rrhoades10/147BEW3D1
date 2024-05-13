# all the functionality i need to run my program
# intended for a list of contacts that will house dictionaries with contact information
# take parameters for contacts list, name, phone and email of our person
def add_contact(contacts, name, phone, email):
    # adds the contact dictionary to the passed in contacts list
    contacts.append({"name": name, "phone": phone, "email": email})    
#  takes contacts as a parameter
def view_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# takes contacts list and a name to search within the dictionary
def search_contacts(contacts, name):
    print()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None
    
# takes contacts list and a name to search and destroy that contact
def delete_contacts(contacts, name):
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            return contacts.pop(i) # pops whatever index i currently is
    return None

# #               0       1        2
# test_list = ["Ryan", "Karen", "Victor"]

# for i, person in enumerate(test_list):
#     if person == "Ryan":
          
#         print(test_list.pop(i))
    
if __name__ == "__main__":
    delete_contacts("hello", "hello again")
else:
    print(False)
