from models.user import User


class MainGuest(User):
    def __init__(self, first_name, last_name, date_of_birth, contact_information, family_members):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.contact_information = contact_information
        self.family_members = family_members
