from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            self.phone = phone
        else:
            raise ValueError("Number must have 10 numbers")

    def __str__(self):
        return str(self.phone)


class Record(Field):
    def __init__(self, name):

        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for i in self.phones:
            if str(i) == phone:
                return i
            elif not str(i) in self.phones:
                return "There are no this phone"

    def remove_phone(self, phone):
        for i in self.phones:
            if str(i) == phone:
                self.phones.remove(i)

    def edit_phone(self, phone, new_phone):

        for i in range(len(self.phones)):
            if str(self.phones[i]) == phone:
                self.phones[i] = Phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = [str(phone) for phone in record.phones]

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]





book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.edit_phone("1234567890", "1112223333")
print(john_record)
found_phone = john_record.find_phone("1112223333")
print(found_phone)