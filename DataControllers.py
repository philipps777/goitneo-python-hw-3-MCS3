from collections import UserDict
from collections import defaultdict
from datetime import datetime, timedelta

from UserInfo import Phone, Name
from UserInfo import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return

    def edit_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for p in self.phones:
            if p.value == old_phone.value:
                p.value = new_phone.value
                return
        raise ValueError("Phone number not found")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        result = f"Contact name: {self.name}, phones: {', '.join(str(p) for p in self.phones)}"
        if self.birthday:
            result += f", birthday: {self.birthday}"
        return result


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(book):
        today = datetime.today()
        next_week = today + timedelta(days=7)

        birthday_dict = defaultdict(list)

        for record in book.data.values():
            name = record.name.value
            birthday = record.birthday.value if record.birthday else None

            if birthday is not None:
                birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
                if today <= birthday_date.replace(year=today.year) <= next_week:
                    weekday = birthday_date.strftime("%A")
                    birthday_dict[weekday].append(name)

                # birthday_dict[birthday_weekday].append(record.name.value)

        for day, names in birthday_dict.items():
            print(f"{day}: {', '.join(names)}")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

