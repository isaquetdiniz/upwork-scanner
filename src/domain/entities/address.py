class Address:
    def __init__(
            self,
            line1: str,
            line2: str,
            city: str,
            state: str,
            postal_code: str,
            country: str,
    ):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
