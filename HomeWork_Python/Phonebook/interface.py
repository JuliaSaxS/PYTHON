from file_writing import writing_scv_txt
from search import search
from change import rewrite_change
from delete import rewrite_delete

def show_main_menu():
    print("\nДобро пожаловать! Выберите необходимый для Вас пункт меню. Приятного пользования!\n\n   *** Меню телефонного списка ***\n"+
          "------------------------------------------\n"+
          "Введите от 1 до 6 (используйте Enter для подтверждения выбора):\n"+
          "1: Просмотр всех записей справочника\n" +
          "2: Добавление новой записи\n"+
          "3: Поиск по справочнику\n"+
          "4: Изменение строки справочника\n"+
          "5: Удаление записи из справочника\n"+
          "6: Выход\n**********************")
    command = input("Команда: >  ")
    if command == "1":
        file = open('Phonebook.csv', "r+", encoding = 'utf-8')
        file_contents = file.read()
        if len(file_contents) == 0:
            print("данных еще не сохранены!")
        else:
            print (file_contents)
        file.close
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()
    elif command == "2":
        writing_scv_txt()
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()
    elif command == "3":
        search()
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()
    elif command == "4":
        rewrite_change()
        user_entry = ("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()
    elif command == "5":
        rewrite_delete()
        user_entry = ("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()
    elif command== "6":
        print("\nСпасибо, что воспользовались нашим справочником!\n")
    else:
        print("Неправильный выбор, пожалуйста, введите от 1 до 6\n")
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        show_main_menu()