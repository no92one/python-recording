list = []

def item_layout (item):
    return f'{item['name']} | {item['amount']} | {item['store']} | {item['description']}'

def start_menu ():
    return input(f'''
--------------------------------
Inköpslista - {len(list)}
--------------------------------

1. See Listan
2. Lägg till vara
3. Ändra vara
4. Ta bort vara

q. Avsluta program 

-> ''').strip()

def item_menu (item, item_index):
    return input(f'''
--------------------------------
Ny vara
--------------------------------

1. Namn         -> {item['name']}
2. Mängd        -> {item['amount']}
3. Butik        -> {item['store']}
4. Anteckning   -> {item['description']}

a. {'Lägg till' if item_index == -1 else 'Uppdatera'}
b. Gå tillbaka

-> ''').strip()

def item_list ():
    print('''
--------------------------------
Varor
--------------------------------
                ''')
    for index, item in enumerate(list):
        print(f'{index + 1}. {item_layout(item)}')
    return input('''
b. Gå tillbaka

Val -> ''').strip()

def add_item (item_index = -1):
    item = {'name': '','amount': '', 'store': '', 'description': ''} if item_index == -1 else list[item_index].copy()
    while True: 
        answer = item_menu(item, item_index)
        
        if answer == '1':
            item['name'] = input('Namn -> ')
        elif answer == '2':
            item['amount'] = input('Mängd -> ')
        elif answer == '3':
            item['store'] = input('Butik -> ')
        elif answer == '4':
            item['description'] = input('Anteckning -> ')
        elif answer.lower() == 'a':
            if item_index == -1:
                list.append(item)
                input(f'{item['name']} - har lagts till i listan.')
            else:
                list[item_index] = item
                input(f'{item['name']} - har uppdaterats.')
            break
        elif answer.lower() == 'b':
            break

def pick_item():
    if len(list) == 0:
        input('Listan är tom.')
        return -1
    else:
        item_index = item_list()

        if item_index.lower() == 'b':
            return -1
        elif item_index.isnumeric() == True:
            item_index = int(item_index)
            if item_index > len(list) or item_index < 1:
                print(f'Finns ingen vara med index {item_index}.')
            else:
                return item_index - 1
        else:
            input(f'{item_index}\nÄr inte ett val.')  

def remove_item ():
    while True:
        item_index = pick_item()

        if item_index == -1:
            break
        elif item_index >= 0:
            del list[item_index]    

def update_item():
    while True:
        item_index = pick_item()

        if item_index == -1:
            break
        elif item_index >= 0:
            add_item(item_index)


while True:
    answer = start_menu()
    
    if answer == '1':
        if len(list) == 0:
            input('Listan är tom.')
        else:
            for item in list:
                print(item_layout(item))
            input('\nTryck enter för att fortätta...')
    elif answer == '2':
        add_item()
    elif answer == '3':
        update_item()
    elif answer == '4':
        remove_item()
    elif answer.lower() == 'q':
        input('Programmet avslutas.')
        break
    else:
        input(f'{answer}\nÄr inte ett val.')