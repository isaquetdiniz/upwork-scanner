class User:
    def __init__(self, username: str, email: str, password: str, security_answer: str):
        self.username = username
        self.email = email
        self.password = password
        self.security_answer = security_answer
