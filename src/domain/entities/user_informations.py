from domain.entities.address import Address


class UserInformations:
    def __init__(
        self,
        account: str,
        first_name: str,
        last_name: str,
        full_name: str,
        email: str,
        phone_number: str,
        picture_url: str,
        address: Address
    ):
        self.id = None
        self.account = account
        self.employer = None
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.birth_date = None
        self.picture_url = picture_url
        self.address = address
        self.ssn = None
        self.marital_status = None
        self.gender = None
        self.metadata = None
        self.created_at = None
        self.updated_at = None
