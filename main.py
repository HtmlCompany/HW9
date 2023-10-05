contacts = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Input your name and phone"
        except KeyError:
            return "No contact"
    return inner

def greating():
    return "How can I help you?"

@input_error
def add_contact(*args):
    contact_name = args[0]
    phone = args[1]
    contacts[contact_name] = phone
    return f"Add {contact_name}, phone {phone}"

@input_error
def change_contact(*args):
    contact_name = args[0]
    new_phone = args[1]
    contact = contacts[contact_name]
    if contact:
        contacts[contact_name] = new_phone
        return f"Change phone {contact_name}, new phone {new_phone}"

@input_error
def see_phone(*args):
    contact_name = args[0]
    return f"New phone number for {contact_name}: {contacts[contact_name]}"

def show_all_contacts():
    return contacts

def undeclared_commands(*args):
    return "Відсутня команда. Спробуйте знову."

def exit_commands(*args):
    return "Good bye"

COMMANDS = {
    greating: "hello",
    add_contact: "add contact",
    change_contact: "change contact",
    see_phone: "phone contact",
    show_all_contacts: "show all",
    exit_commands: ("good bye", "close", "exit")
}

def checking_commands(text:str):
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return undeclared_commands, []

def main():
    while True:
        user_input = input(">")
        func, data = checking_commands(user_input)
        print(func(*data))
        if func == exit_commands:
            break

if __name__ == "__main__":
    main()