from datetime import datetime
from Field import Field


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and phone.isdigit():
            if phone:
                super().__init__(phone)
            else:
                raise ValueError("Invalid phone number format")

    @property
    def phone(self):
        raise AttributeError('This property has no getter')

    @phone.setter
    def phone(self, phone):
        self.__init__(phone)


class Birthday(Field):
    def __init__(self, birthday):
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            return

        if birthday:
            super().__init__(birthday)
        else:
            raise ValueError("Invalid birthday format. Use DD.MM.YYYY")

    @property
    def birthday(self):
        raise AttributeError('This property has no getter')

    @birthday.setter
    def birthday(self, birthday):
        self.__init__(birthday)