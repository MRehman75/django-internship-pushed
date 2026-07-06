from datetime import datetime, date


class Contact:
    def __init__(
        self,
        name,
        phone,
        email,
        birthday,
        address,
        tags=None,
        created_at=None,
    ):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday 
        self.address = address
        self.tags = tags if tags else []
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "birthday": self.birthday,
            "address": self.address,
            "tags": self.tags,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            birthday=data["birthday"],
            address=data["address"],
            tags=data.get("tags", []),
            created_at=data.get("created_at"),
        )

    def birthday_this_year(self):
        """Return birthday as a date object for the current year."""
        birthday = datetime.strptime(self.birthday, "%Y-%m-%d").date()
        today = date.today()

        try:
            return birthday.replace(year=today.year)
        except ValueError:
            
            return birthday.replace(year=today.year, day=28)

    def __str__(self):
        tags = ", ".join(self.tags) if self.tags else "None"

        return (
            f"\nName       : {self.name}\n"
            f"Phone      : {self.phone}\n"
            f"Email      : {self.email}\n"
            f"Birthday   : {self.birthday}\n"
            f"Address    : {self.address}\n"
            f"Tags       : {tags}\n"
            f"Created At : {self.created_at}"
        )