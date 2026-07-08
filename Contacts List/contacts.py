# Stores the current contact list.
# Contacts are represented as 5-digit strings.
contacts = ['12345', '13452', '17653']


def main():
    # Validate the user's menu choice before processing it.
    if conditions():
        print('Fail')
        return 'Exit'

    # Execute the selected menu option.
    if user_input == '1':
        add_contact()

    if user_input == '2':
        search_contact()

    if user_input == '3':
        list_contact()

    # Exit the program.
    if user_input == '4':
        return 'Exit'


def conditions():
    # Ensure the menu input is numeric.
    if user_input.isdigit():

        # Only options 1–4 are valid.
        if 0 >= int(user_input) or int(user_input) > 4:
            print('Input must be 1 to 4')
            return True
        else:
            return False

    # Reject non-numeric menu inputs.
    else:
        print('Input must be digits')
        return True


def add_contact():
    # Prompt the user for a new contact number.
    new_contact = input('Add a contact: ')

    # A valid contact must start with "1" and contain exactly 5 digits.
    if new_contact.startswith('1') and len(new_contact) == 5:

        # Prevent duplicate contacts.
        if new_contact not in contacts:
            contacts.append(new_contact)
            print('Successfully added!', new_contact)
        else:
            print('Contact already in contact list!')

    else:
        print('It must be 5 digits and starts with a 1')


def search_contact():
    # Ask the user for the contact number to search.
    search_contact = input('Input the contact you want to search: ')

    # Validate the contact format before searching.
    if search_contact.startswith('1') and len(search_contact) == 5:

        if search_contact in contacts:
            print('Contact is in contact list!')
        else:
            print('Contact is not in contact list')

    else:
        print('It must be 5 digits and starts with a 1')


def list_contact():
    # Display every saved contact.
    for contact in contacts:
        print(contact)


# Main program loop.
# Continues until the user chooses to exit.
while True:
    user_input = input('''
    What do you want to do?
    1. Add a contact
    2. Search a contact
    3. List contacts
    4. Exit
    ''')

    Exit = main()

    if Exit == 'Exit':
        break