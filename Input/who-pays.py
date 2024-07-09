import random

nameList = []  

while True:
    print("\nWho pays?")
    print("-------------------")
    print(f"\nNamnlista = {nameList}")
    print("\n1. Lägg till namn")
    if len(nameList) > 0:
        print("2. Töm namnlistan")
    if len(nameList) > 1:
        print("3. Välj ett random namn")
    print("q. Avsluta programmet")
    choice = input("\n-> ")
    choice = choice.strip().lower()

    if choice == "1":
        name = input("Skriv ett namn: ")
        nameList.append(name)
    elif choice == "2" and len(nameList) > 0:
        nameList.clear()
    elif choice == "3" and len(nameList) > 1:
        print(f"{random.choice(nameList)} ska betala idag!")
    elif choice == "q":
        break
    else:
        print("Du måste göra ett giltigt menyval.")  

    input("\nTryck enter för att fortsätta...")