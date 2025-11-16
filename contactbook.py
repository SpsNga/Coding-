print("Welcome to the Contact Book !")
contacts = {}
def add_contacts() :
        a = input("enter the name of contact : ")
        b = (input("enter contact no. of the contact : "))
        if len(b) != 10:
            print("number is not of 10 digits ! ")
        else :
            contacts[a ] = b
            print("contact saved ")
            print(contacts)
            
def delete_contacts() :
     a = input("Which contact u wanna delete ?  ")
     del contacts[a]
     print("Contact deleted !")
     print(contacts)


def list_contacts() :
     print("Here are the contacts you have :")
     print(contacts)

def search_contacts() :
     a = input("Enter the name of the contact you wanna delete : ")   
     if a in contacts :
          print("No.", contacts[a])  
     else :
          print("contact not found !")
  
while True :
     print("\nWhat do u wanna do ?" )
     a = input("1. Add contact , 2. Delete Contact , 3. List Contacts , 4. Search Contacts , 5. Exit : ")
     if a == "1" :
          add_contacts()
     elif a == "2" :
          delete_contacts()
     elif a == "3" :
          list_contacts()
     elif a == "4" :
          search_contacts()
     else :
          break
