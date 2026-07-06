import json
from contact import Contact


def load_contacts(filename="contacts.json"):
    """
    Load contacts from a JSON file.
    Returns a list of Contact objects.
    """
    contacts = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                contacts.append(Contact.from_dict(item))

    except FileNotFoundError:
       
        pass

    except json.JSONDecodeError:
        print("Error: contacts.json contains invalid JSON. Starting with an empty contact list.")

    except Exception as e:
        print(f"Error loading contacts: {e}")

    return contacts


def save_contacts(contacts, filename="contacts.json"):
    """
    Save a list of Contact objects to a JSON file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                [contact.to_dict() for contact in contacts],
                file,
                indent=4,
            )

    except Exception as e:
        print(f"Error saving contacts: {e}")