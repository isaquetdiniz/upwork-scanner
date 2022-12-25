from abc import ABC, abstractclassmethod
from src.domain.entities.user import User
from src.domain.entities.job import Job


class JobRepository(ABC):
    @abstractclassmethod
    def get_by_user(self, user: User) -> list[Job]:
        raise (NotImplementedError)
