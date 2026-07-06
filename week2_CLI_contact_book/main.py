from contact import Contact
from contact_book import ContactBook
from storage import load_contacts, save_contacts
from utiles import (
    validate_name,
    validate_phone,
    validate_email,
    validate_birthday,
    validate_tags,
)


def menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. View Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Search Contact")
    print("7. Birthdays This Month")
    print("8. Birthdays Next 7 Days")
    print("9. Export to CSV")
    print("0. Exit")


def add_contact(book):
    try:
        name = validate_name(input("Name: "))
        phone = validate_phone(input("Phone: "))
        email = validate_email(input("Email: "))
        birthday = validate_birthday(input("Birthday (YYYY-MM-DD): "))
        address = input("Address: ").strip()
        tags = validate_tags(input("Tags (comma separated): "))

        contact = Contact(
            name,
            phone,
            email,
            birthday,
            address,
            tags,
        )

        book.add_contact(contact)
        save_contacts(book.contacts)
        print("Contact added successfully!")

    except ValueError as e:
        print(f"Error: {e}")


def view_all(book):
    contacts = book.get_all_contacts()

    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\n----- Contact {i} -----")
        print(contact)


def view_single(book):
    name = input("Enter name: ")

    contact = book.get_contact(name)

    if contact:
        print(contact)
    else:
        print("Contact not found.")


def edit_contact(book):
    name = input("Enter contact name to edit: ")

    contact = book.get_contact(name)

    if not contact:
        print("Contact not found.")
        return

    try:
        phone = input(f"Phone ({contact.phone}): ").strip()
        email = input(f"Email ({contact.email}): ").strip()
        birthday = input(f"Birthday ({contact.birthday}): ").strip()
        address = input(f"Address ({contact.address}): ").strip()
        tags = input(f"Tags ({', '.join(contact.tags)}): ").strip()

        book.edit_contact(
            name,
            phone=validate_phone(phone) if phone else None,
            email=validate_email(email) if email else None,
            birthday=validate_birthday(birthday) if birthday else None,
            address=address if address else None,
            tags=validate_tags(tags) if tags else None,
        )

        print("Contact updated successfully!")

    except ValueError as e:
        print(f"Error: {e}")


def delete_contact(book):
    name = input("Enter contact name: ")

    if book.delete_contact(name):
        print("Contact deleted.")
    else:
        print("Contact not found.")


def search_contact(book):
    keyword = input("Search: ")

    results = book.search(keyword)

    if not results:
        print("No matching contacts.")
        return

    for contact in results:
        print(contact)


def show_birthdays_month(book):
    contacts = book.birthdays_this_month()

    if not contacts:
        print("No birthdays this month.")
        return

    for contact in contacts:
        print(contact)


def show_birthdays_week(book):
    contacts = book.birthdays_next_7_days()

    if not contacts:
        print("No birthdays in the next 7 days.")
        return

    for contact in contacts:
        print(contact)


def export_contacts(book):
    try:
        book.export_csv()
        print("Contacts exported to contacts_export.csv")
    except Exception as e:
        print(f"Export failed: {e}")


def main():
    book = ContactBook()

    book.contacts = load_contacts()

    while True:
        menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_contact(book)

        elif choice == "2":
            view_all(book)

        elif choice == "3":
            view_single(book)

        elif choice == "4":
            edit_contact(book)

        elif choice == "5":
            delete_contact(book)

        elif choice == "6":
            search_contact(book)

        elif choice == "7":
            show_birthdays_month(book)

        elif choice == "8":
            show_birthdays_week(book)

        elif choice == "9":
            export_contacts(book)

        elif choice == "0":
            save_contacts(book.contacts)
            print("Contacts saved.")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()