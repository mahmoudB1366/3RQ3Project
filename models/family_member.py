from models.user import User


class FamilyMember(User):
    def __init__(self, first_name, last_name, date_of_birth, relation):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.relation = relation

