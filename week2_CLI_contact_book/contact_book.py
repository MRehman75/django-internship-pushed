from datetime import date, timedelta
from contact import Contact
import csv


class ContactBook:
    def __init__(self):
        self.contacts = []


    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts

    def get_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def edit_contact(
        self,
        name,
        phone=None,
        email=None,
        birthday=None,
        address=None,
        tags=None,
    ):
        contact = self.get_contact(name)

        if not contact:
            return False

        if phone:
            contact.phone = phone

        if email:
            contact.email = email

        if birthday:
            contact.birthday = birthday

        if address:
            contact.address = address

        if tags is not None:
            contact.tags = tags

        return True

    def delete_contact(self, name):
        contact = self.get_contact(name)

        if contact:
            self.contacts.remove(contact)
            return True

        return False


    def search(self, keyword):
        keyword = keyword.lower()
        results = []

        for contact in self.contacts:
            if (
                keyword in contact.name.lower()
                or keyword in contact.phone.lower()
                or keyword in contact.email.lower()
                or any(keyword in tag.lower() for tag in contact.tags)
            ):
                results.append(contact)

        return results


    def birthdays_this_month(self):
        month = date.today().month

        return [
            contact
            for contact in self.contacts
            if contact.birthday_this_year().month == month
        ]

    def birthdays_next_7_days(self):
        today = date.today()
        end = today + timedelta(days=7)

        results = []

        for contact in self.contacts:
            birthday = contact.birthday_this_year()

            if today <= birthday <= end:
                results.append(contact)

        return results


    def export_csv(self, filename="contacts_export.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "Name",
                    "Phone",
                    "Email",
                    "Birthday",
                    "Address",
                    "Tags",
                    "Created At",
                ]
            )

            for contact in self.contacts:
                writer.writerow(
                    [
                        contact.name,
                        contact.phone,
                        contact.email,
                        contact.birthday,
                        contact.address,
                        ", ".join(contact.tags),
                        contact.created_at,
                    ]
                )