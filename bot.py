def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() 
    return cmd, *args


def get_command(input):
    commands = {
        "add": add_contact,
        "all": show_all,
        "change": change_contact,
        "hello": greeting,
        "phone": show_phone,
        "remove": remove_contact,
    }

    command = commands.get(input)
    if not command:
        return invalid_command
    return command


def add_contact(contacts, *args):
    name, phone_number = args
    contacts[name] = phone_number
    return "Contact added."


def change_contact(contacts, *args):
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    return "Contact not found."


def greeting(*_):
    return "How can I help you?"


def invalid_command(*_):
    return "Invalid command."


def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return "Contact removed."
    return "Contact not found."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts):
    if contacts:
        result = "All contacts: "
        for name, phone_number in contacts.items():
            result += f"\n{name}: {phone_number}"
            return result
    return "No contacts."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        print(get_command(command)(contacts, *args))


if __name__ == "__main__":
    main()
