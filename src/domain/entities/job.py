from domain.entities.client import Client


class Job:
    def __init__(
        self,
        title: str,
        description: str,
        tags: list[str],
        level: str,
        payment: str,
        client: Client
    ):
        self.title = title
        self.description = description
        self.tags = tags
        self.level = level
        self.payment = payment
        self.client = client
