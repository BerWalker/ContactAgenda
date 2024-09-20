# Contact Agenda

## Introduction
This program is a simple contact management system. It allows users to add, edit, delete, import, and export contacts. This project is part of a bonus module from the Solyd course.

## Data Structure
- **AGENDA**: A dictionary that stores contacts, where each contact is a key, and its value is a dictionary containing information (phone number, email, and address).

## Functions

### `show_contacts()`
Displays all contacts in the agenda. If the agenda is empty, it informs that there are no contacts.

### `display_contact(contact)`
Displays the information of a specific contact. If the contact does not exist, it shows an error message.

### `get_contact_details()`
Prompts the user to enter the phone number, email, and address of a contact. Returns these details as a tuple.

### `add_or_edit_contact(contact, phone, email, address)`
Adds a new contact or edits an existing one. Updates the `AGENDA` dictionary and saves the changes.

### `delete_contact(contact)`
Removes a contact from the agenda. Displays a confirmation message or an error if the contact does not exist.

### `export_contacts(file_name)`
Exports all contacts to a CSV file. Each line contains the name, phone number, email, and address of the contact.

### `import_contacts(file_name)`
Imports contacts from a CSV file. Adds each contact to the agenda. Displays error messages if the file is not found or if another error occurs.

### `save()`
Saves the current state of the agenda to a default CSV file named `database.csv`.

### `load()`
Loads contacts from the `database.csv` file into the agenda when the program starts. Displays how many contacts were loaded or an error message if the file is not found.

### `print_menu()`
Displays the main menu with the available options for the user to interact with the agenda.

## Program Flow
1. The program loads contacts from the `database.csv` file at startup.
2. A main loop displays the menu and waits for user input.
3. Depending on the chosen option, the program executes the corresponding function:
   - Show contacts
   - Search for a contact
   - Add a new contact
   - Edit an existing contact
   - Delete a contact
   - Export contacts to a CSV file
   - Import contacts from a CSV file
   - Exit the program

## Final Considerations
This program provides a simple interface for managing contacts, allowing for easy data manipulation. The robustness of error handling ensures that the user receives helpful feedback during execution.
