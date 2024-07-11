def show_menu():
    print("\n--- Meny ---")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Avsluta")
    choice = input("Välj ett alternativ (1-5): ")
    return choice

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Fel: Division med noll är inte tillåtet"

def get_numbers():
    a = float(input("Ange det första numret: "))
    b = float(input("Ange det andra numret: "))
    return a, b

while True:
    choice = show_menu()

    if choice == '1':
        a, b = get_numbers()
        result = add(a, b)
        print("Addition")
        print(f"Resultatet är: {result}")
    
    elif choice == '2':
        a, b = get_numbers()
        result = subtract(a, b)
        print("Subtraktion")
        print(f"Resultatet är: {result}")

    elif choice == '3':
        a, b = get_numbers()
        result = multiply(a, b)
        print("Multiplikation")
        print(f"Resultatet är: {result}")

    elif choice == '4':
        a, b = get_numbers()
        result = divide(a, b)
        print("Division") 
        print(f"Resultatet är: {result}")

    elif choice == '5':
        print("Avslutar programmet...")
        break

    else:
        print("Ogiltigt val, försök igen.")
