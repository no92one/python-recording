list = []

while True:

    answer = input(f'''
--------------------------------
Inköpslista - {len(list)}
--------------------------------

1. See Listan
2. Lägg till vara
3. Ändra vara
4. Ta bort vara

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
        item = {'name': '','amount': '', 'store': '', 'description': ''}
        while True: 
            answer = input(f'''
--------------------------------
Ny vara
--------------------------------

1. Namn         -> {item['name']}
2. Mängd        -> {item['amount']}
3. Butik        -> {item['store']}
4. Anteckning   -> {item['description']}

a. Lägg till
b. Gå tillbaka

-> ''').strip()
        
            if answer == '1':
                item['name'] = input('Namn -> ')
            elif answer == '2':
                item['amount'] = input('Mängd -> ')
            elif answer == '3':
                item['store'] = input('Butik -> ')
            elif answer == '4':
                item['description'] = input('Anteckning -> ')
            elif answer.lower() == 'a':
                list.append(item)
                input(f'{item['name']} - har lagts till i listan.')
                break
            elif answer.lower() == 'b':
                break
    elif answer == '3':
        while True:
            if len(list) == 0:
                input('Listan är tom.')
                break
            else:
                print('''
--------------------------------
Varor
--------------------------------
                ''')
                for index, item in enumerate(list):
                    print(f'{index + 1}. {item['name']}')
                updateIndex = input('''
b. Gå tillbaka

Ta bort -> ''').strip()

                if updateIndex.lower() == 'b':
                    break
                elif updateIndex.isnumeric() == True:
                    updateIndex = int(updateIndex)
                    if updateIndex > len(list) or updateIndex < 1:
                        print(f'Finns ingen vara med index {updateIndex}.')
                    else:
                        item = list[updateIndex]
                        while True: 
                            answer = input(f'''
--------------------------------
Ny vara
--------------------------------

1. Namn         -> {item['name']}
2. Mängd        -> {item['amount']}
3. Butik        -> {item['store']}
4. Anteckning   -> {item['description']}

a. Uppdatera {item['name']}
b. Gå tillbaka

-> ''').strip()
        
                            if answer == '1':
                                item['name'] = input('Namn -> ')
                            elif answer == '2':
                                item['amount'] = input('Mängd -> ')
                            elif answer == '3':
                                item['store'] = input('Butik -> ')
                            elif answer == '4':
                                item['description'] = input('Anteckning -> ')
                            elif answer.lower() == 'a':
                                list[updateIndex] = item
                                input(f'{item['name']} - har uppdaterats.')
                                break
                            elif answer.lower() == 'b':
                                break
                        
                else:
                    input(f'{updateIndex}\nÄr inte ett val.')
    elif answer == '4':
        while True:
            if len(list) == 0:
                input('Listan är tom.')
                break
            else:
                print('''
--------------------------------
Varor
--------------------------------
                ''')
                for index, item in enumerate(list):
                    print(f'{index + 1}. {item['name']}')
                remove = input('''
b. Gå tillbaka

Ta bort -> ''').strip()

                if remove.lower() == 'b':
                    break
                elif remove.isnumeric() == True:
                    remove = int(remove)
                    if remove > len(list) or remove < 1:
                        print(f'Finns ingen vara med index {remove}.')
                    else:
                        del list[remove - 1]
                else:
                    input(f'{remove}\nÄr inte ett val.')
    else:
        input(f'{answer}\nÄr inte ett val.')
            