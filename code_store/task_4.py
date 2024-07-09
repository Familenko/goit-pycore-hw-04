"""
Task 4
"""


import json


def hello(arg: tuple = None) -> None:
    """
    This function prints a greeting message.
    """
    print("How can I help you?")


def load_contacts(filename: str = 'contacts.json') -> dict:
    """
    This function loads contacts from a file.
    :param filename: str
    :return: dict
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts_dict: dict, filename: str = 'contacts.json') -> None:
    """
    This function saves contacts to a file.
    :param contacts_dict: dict
    :param filename: str
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(contacts_dict, file, ensure_ascii=False, indent=4)


def add_contact(args: tuple, filename: str = 'contacts.json') -> None:
    """
    This function adds a contact to the contacts list.
    :param args: tuple
    :param filename: str
    :return: None
    """
    if len(args) == 2:
        name, phone = args
        contacts = load_contacts(filename)
        contacts[name] = phone
        save_contacts(contacts, filename)
        print("Contact added.")
    else:
        print("Invalid command format for add. Write 'add <name> <phone>'")


def change_contact(args: tuple, filename: str = 'contacts.json') -> None:
    """
    This function changes a contact's phone number.
    :param args: tuple
    :param filename: str
    :return: None
    """
    if len(args) == 2:
        name, phone = args
        contacts = load_contacts(filename)
        if name in contacts:
            contacts[name] = phone
            save_contacts(contacts, filename)
            print("Contact updated.")
        else:
            print("Contact not found.")
    else:
        print("Invalid command format for change. Write 'change <name> <phone>'")


def show_phone(args: tuple, filename: str = 'contacts.json') -> None:
    """
    This function shows a contact's phone number.
    :param args: tuple
    :param filename: str
    :return: None
    """
    if len(args) == 1:
        name = args[0]
        contacts = load_contacts(filename)
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found.")
    else:
        print("Invalid command format for phone. Write 'phone <name>'")


def show_all_contacts(filename: str = 'contacts.json') -> None:
    """
    This function shows all contacts.
    :param filename: str
    :return: None
    """
    contacts = load_contacts(filename)
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def parse_input(user_input: str) -> tuple:
    """
    This function parses user input.
    :param user_input: str
    :return: tuple
    """
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args
