CONTACTS = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return inner

@input_error
def hello(customer_input):
    return "How can I help you?"

@input_error
def add(customer_input):
    action, name, phone = customer_input.split()
    if name not in CONTACTS:
        CONTACTS[name] = phone
        return "Contact added successfully!"
    raise ValueError("Contact with such name already exists.")

@input_error
def change(customer_input):
    action, name, phone = customer_input.split()
    if name in CONTACTS:
        CONTACTS[name] = phone
        return "Contact updated successfully!"
    else:
        return "Contact with such name does not exist."

@input_error
def get_phone(customer_input):
    action, name = customer_input.split()
    return CONTACTS.get(name, "Contact not found.")

@input_error
def show_all(customer_input):
    if customer_input != 'show all':
        raise ValueError("Unknown action. Please, try again.")
    
    if len(CONTACTS) == 0:
        return "Contacts library is empty."
    
    return "\n".join([f"{k}: {v}" for k, v in CONTACTS.items()])

@input_error
def bye_bye(customer_input):
    if customer_input in ['good bye', 'exit', 'close']:
        return "Good bye!"
    raise ValueError("Unknown action. Please, try again.")

ACTIONS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": get_phone,
    "show": show_all,
    "good": bye_bye,
    "exit": bye_bye,
    "close": bye_bye
}

@input_error
def get_action(customer_input):
    action = customer_input.split()[0]
    return ACTIONS.get(action, lambda x: f"Unknown action '{x}'. Please, try again.")

def main():
    while True:
        try:
            customer_input = input(">>>").lower().strip()
            handler = get_action(customer_input)
            result = handler(customer_input)
            print(result)
            if result == "Good bye!":
                break

        except (IndexError, ValueError, KeyError) as e:
            print(str(e))

if __name__ == '__main__':
    main()
