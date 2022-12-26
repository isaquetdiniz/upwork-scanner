from abc import ABC, abstractclassmethod
from domain.entities.user import User
from domain.entities.job import Job


class JobRepository(ABC):
    @abstractclassmethod
    def get_by_user(self, user: User) -> list[Job]:
        raise (NotImplementedError)
