from FIle_manager.journal import Journal, Entry

def main_menu(journal):
    while True:
        print("\nГлавное меню:")
        print("1. Добавить запись")
        print("2. Просмотреть записи")
        print("3. Поиск записей")
        print("4. Удалить запись")
        print("5. Обновить запись")
        print("6. Выход")

        choice = input("Выберите действие: ")
        if choice == '1':
            date = input("Введите дату: ")
            author = input("Введите автора: ")
            message = input("Введите сообщение: ")
            entry = Entry(date, author, message)
            journal.add_entry(entry)
            print("Запись успешно добавлена.")
        elif choice == '2':
            print("\nЗаписи в журнале:")
            print(journal)
        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска: ")
            results = journal.search_entries(keyword)
            if results:
                print("\nРезультаты поиска:")
                for entry in results:
                    print(entry)
            else:
                print("Записи не найдены.")
        elif choice == '4':
            index = int(input("Введите индекс записи для удаления: "))
            journal.delete_entry(index)
            print("Запись успешно удалена.")
        elif choice == '5':
            index = int(input("Введите индекс записи для обновления: "))
            date = input("Введите новую дату (оставьте пустым, если изменения не требуются): ")
            author = input("Введите нового автора (оставьте пустым, если изменения не требуются): ")
            message = input("Введите новое сообщение (оставьте пустым, если изменения не требуются): ")
            journal.update_entry(index, date if date else None, author if author else None, message if message else None)
            print("Запись успешно обновлена.")
        elif choice == '6':
            break


if __name__ == "__main__":
    journal_path = "journal.txt"
    journal = Journal(journal_path)
    main_menu(journal)
