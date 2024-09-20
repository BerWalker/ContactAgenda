AGENDA = {}


def show_contacts():
    if AGENDA:
        for contact in AGENDA:
            display_contact(contact)
    else:
        print('>>>> Empty agenda')


def display_contact(contact):
    try:
        info = AGENDA[contact]
        print(f'Name: {contact}')
        print(f'Phone: {info["phone"]}')
        print(f'Email: {info["email"]}')
        print(f'Address: {info["address"]}')
        print('====================================')
    except KeyError:
        print('>>>> Contact does not exist')
    except Exception as error:
        print('>>>> An unexpected error occurred')
        print(error)


def get_contact_details():
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')
    address = input('Enter address: ')
    return phone, email, address


def add_or_edit_contact(contact, phone, email, address):
    AGENDA[contact] = {
        'phone': phone,
        'email': email,
        'address': address,
    }
    save()
    print(f'\n>>>> Contact {contact} successfully added/edited\n')


def delete_contact(contact):
    try:
        AGENDA.pop(contact)
        save()
        print(f'\n>>>> Contact {contact} successfully deleted\n')
    except KeyError:
        print('>>>> Contact does not exist')
    except Exception as error:
        print('>>>> An unexpected error occurred')
        print(error)


def export_contacts(file_name):
    try:
        with open(file_name, 'w') as file:
            for contact in AGENDA:
                info = AGENDA[contact]
                file.write(f"{contact},{info['phone']},{info['email']},{info['address']}\n")
        print('>>>> Agenda successfully exported')
    except Exception as error:
        print('>>>> An error occurred while exporting contacts')
        print(error)


def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, phone, email, address = line.strip().split(',')
                add_or_edit_contact(name, phone, email, address)
    except FileNotFoundError:
        print('>>>> File not found')
    except Exception as error:
        print('>>>> An unexpected error occurred')
        print(error)


def save():
    export_contacts('database.csv')


def load():
    try:
        with open('database.csv', 'r') as file:
            for line in file:
                name, phone, email, address = line.strip().split(',')
                AGENDA[name] = {'phone': phone, 'email': email, 'address': address}
        print('>>>> Database loaded successfully')
        print(f'>>>> {len(AGENDA)} contacts loaded')
    except FileNotFoundError:
        print('>>>> File not found')
    except Exception as error:
        print('>>>> An unexpected error occurred')
        print(error)


def print_menu():
    print('==========================================')
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - Delete contact')
    print('6 - Export contacts to CSV')
    print('7 - Import contacts from CSV')
    print('0 - Close agenda')
    print('==========================================')


# PROGRAM START
load()
while True:
    print_menu()
    option = input('Choose an option: ')

    match option:
        case '1':
            show_contacts()
        case '2':
            contact = input('Enter contact name: ')
            display_contact(contact)
        case '3':
            contact = input('Enter contact name: ')
            if contact in AGENDA:
                print('>>>> Contact already exists')
            else:
                phone, email, address = get_contact_details()
                add_or_edit_contact(contact, phone, email, address)
        case '4':
            contact = input('Enter contact name: ')
            if contact in AGENDA:
                print(f'>>>> Editing contact: {contact}')
                phone, email, address = get_contact_details()
                add_or_edit_contact(contact, phone, email, address)
            else:
                print('>>>> Contact does not exist')
        case '5':
            contact = input('Enter contact name: ')
            delete_contact(contact)
        case '6':
            file_name = input('Enter file name to export: ')
            export_contacts(file_name)
        case '7':
            file_name = input('Enter file name to import: ')
            import_contacts(file_name)
        case '0':
            print('>>>> Closing program')
            break
        case _:
            print('>>>> Invalid option')
