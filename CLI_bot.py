def error_decorator(message_type):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                if message_type == "error":
                    return "\033[91mError:\033[N Give me name and phone please.\033[0m"
                elif message_type == "warning":
                    return "\033[93mWarning:\033[N Contact or phone number already exists. Please use unique name and phone number\033[0m"
            except KeyError:
                if message_type == "error":
                    return "\033[91mError:\033[N Contact does not exist!\033[0m"
                elif message_type == "warning":
                    return "\033[91mError:\033[N No contacts found! \033[0m"
            except IndexError:
                if message_type == "error":
                    return "\033[91mError:\033[N Invalid number of arguments!\033[0m"

        return inner

    return decorator


@error_decorator("warning")
def add_contact(args, contacts):
    name, phone = args
    if phone in contacts.values() or name in contacts:
        raise ValueError
    contacts[name] = phone
    return "Contact added."


@error_decorator("error")
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@error_decorator("error")
def get_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]


@error_decorator("error")
def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return None, []


@error_decorator("warning")
def get_all_contacts(contacts):
    if not contacts:
        raise KeyError
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
