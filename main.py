from DataControllers import Record, AddressBook


def main():

    book = AddressBook()
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) == 2:
                name, phone = args
                record = Record(name)
                record.add_phone(phone)
                book.add_record(record)
                print("Contact added.")
            else:
                print("Invalid command. Use 'add [name] [phone]'.")

        elif command == "change":
            if len(args) == 2:
                name, phone = args
                record = book.find(name)
                if record:
                    record.edit_phone(record.phones[0].value, phone)
                    print("Contact updated.")
                else:
                    print("Contact not found.")
            else:
                print("Invalid command. Use 'change [name] [phone]'.")

        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                record = book.find(name)
                if record:
                    phone = record.phones[0].value
                    print(phone)
                else:
                    print("Contact not found.")
            else:
                print("Invalid command. Use 'phone [name]'.")

        elif command == "all":
            result = str(book)
            print(result)

        elif command == "add-birthday":
            if len(args) == 2:
                name, birthday = args
                record = book.find(name)
                if record:
                    record.add_birthday(birthday)
                    print("Birthday added.")
                else:
                    print("Contact not found.")
            else:
                print(
                    "Invalid command. Use 'add-birthday [name] [DD.MM.YYYY]'.")

        elif command == "show-birthday":
            if len(args) == 1:
                name = args[0]
                record = book.find(name)
                if record and record.birthday:
                    print(f"{name}'s birthday is on {record.birthday.value}")
                else:
                    print("Contact not found or birthday not set.")
            else:
                print("Invalid command. Use 'show-birthday [name]'.")

        elif command == "birthdays":
            book.get_birthdays_per_week()

        else:
            print("Invalid command.")

        # save_address_book(book, 'address_book.json')


if __name__ == "__main__":
    main()
