from os.path import exists
from scv_creating import creating
from interface import show_main_menu

path = 'Phonebook.txt'

try:                        
    file = open(path, 'r')  
except IOError:             
    print('A new phone directory has been created -> Phonebook.txt')
    file = open(path, 'w')
finally:                    
    file.close()

valid = exists('Phonebook.csv')
if not valid:
    creating()

show_main_menu()