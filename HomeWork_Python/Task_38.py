# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных.

def print_entries(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def input_entries(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        entry_id = 0
        for line in data:
            if line != '':
                entry_id = line.split(';', 1)[0]
        print('Enter contacts last name, first name, patronymic, phone number (using a space).')
        line = f'{int(entry_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('adding')
        if confirm == 'y':
            data.write(line)

def find_char():
    print('Select a characteristic: ')
    print('0 - id, 1 - last name, 2 - name, 3 - patronymic, 4 - phone number, q - quit')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Input error.')
        print('Select a characteristic: ')
        print('0 - id, 1 - last name, 2 - name, 3 - patronymic, 4 - phone number, q - quit')
        char = input()
    if char != 'q':
        inp = input('Enter a value\n')
        return char, inp
    else:
        return 'q', 'q'

def find_entries(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Not found.")
        return printed

def check_id_entry(file_name: str, text: str):
    choice = input(f'Do you know the id of the entry you want to {text}? 1 - yes, 2 - no, q - quit\n')
    while choice not in ('1', 'q'):
        if choice != '2':
            print('Input error.')
        else:
            find_entries(path, *find_char())
        choice = input(f'Do you know the id of the entry you want to {text}? 1 - yes, 2 - no, q - quit\n')
    if choice == '1':
        entry_id = input('Input id, q - quit\n')
        while not find_entries(file_name, '0', entry_id) and entry_id != 'q':
            entry_id = input('Input id, q - quit\n')
        return entry_id
    return choice

def confirmation(text: str):
    confirm = input(f"Confirm {text} the entry: y - yes, n - no\n")
    while confirm not in ('y', 'n'):
        print('Input error.')
        confirm = input(f"Confirm {text} the entry: y - yes, n - no\n")
    return confirm

def replace_entry_line(file_name: str, entry_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if entry_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_entry(file_name: str):
    entry_id = check_id_entry(file_name, 'change')
    if entry_id != 'q':
        replaced_line = f'{int(entry_id)};' + ';'.join(
            input('Enter contacts last name, first name, patronymic, phone number (using a space)\n').split()[:4]) + ';\n'
        confirm = confirmation('change')
        if confirm == 'y':
            replace_entry_line(file_name, entry_id, replaced_line)

def delete_entry(file_name: str):
    entry_id = check_id_entry(file_name, 'delete')
    if entry_id != 'q':
        confirm = confirmation('deleting')
        if confirm == 'y':
            replace_entry_line(file_name, entry_id, '')

path = 'phone_book.txt'

try:                        
    file = open(path, 'r')  
except IOError:             
    print('A new phone directory has been created -> phone_book.txt')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'viewing',
           '2': 'writing',
           '3': 'search',
           '4': 'change',
           '5': 'deleting',
           'q': 'quit'}

action = None
while action != 'q':
    print('Select an action', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Select an action', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Input error.')
    if action != 'q':
        if action == '1':
            print_entries(path)
        elif action == '2':
            input_entries(path)
        elif action == '3':
            find_entries(path, *find_char())
        elif action == '4':
            change_entry(path)
        elif action == '5':
            delete_entry(path)