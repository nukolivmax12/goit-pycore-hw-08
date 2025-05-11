import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def main():
    book = load_data()
    print('''Вітаю в додатку телефонної книги.\nКоманди:\nadd_contact\nshow_all_contacts\nquit\n''')
    while True:
        response = input('> ')
        if response == 'quit':
            save_data(book)
            break
        if response == 'show_all_contacts':
            print(book.show_contacts())
        if response == 'add_contact':
            add_record(book)
        else: print('Unknown command')

def add_record(book):
    while True:
        name = input("Введіть ім'я контакту: ")
        last_name = input("Введіть прізвище контакту: ")
        email = input("Введіть електронну адресу контакту: ")
        number = input("Введіть номер контакту: ")
        is_favorite = input("Додати контакт в улюблені? (yes/no): ")
        if is_favorite == 'yes':
            is_favorite = True
        else: is_favorite = False
        break
    book.add_contact(name, last_name, email, number, is_favorite)
    save_data(book)
    print("Контакт успішно додано!")
    main()

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, lastname, email, number, is_favorite):
        contact = {
            "name": name,
            "lastname": lastname,
            "email": email,
            "number": number,
            "is_favorite": is_favorite
        }
        self.contacts.append(contact)

    def show_contacts(self):
        return self.contacts


if __name__ == '__main__':
    main()
