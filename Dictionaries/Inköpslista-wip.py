list = []

while True:

    answer = input(f'''
--------------------------------
Inköpslista
--------------------------------

1. See Listan
2. Lägg till vara
3. Ta bort vara

q. Avsluta program 

-> ''').strip() 
    
    if answer.lower() == 'q':
        input('Programmet avslutas.')
        break
    elif answer == '1':
        if len(list) == 0:
            input('Listan är tom.')
        else:
            for item in list:
                print(item)
            input('\nTryck enter för att fortätta...')
    elif answer == '2':
        print('Lägg till kommer snart...')
    elif answer == '3':
        print('Ta bort kommer snart...')
    else:
        input(f'{answer}\nÄr inte ett val.')
            