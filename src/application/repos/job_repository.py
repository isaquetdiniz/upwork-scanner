from abc import ABC, abstractclassmethod

from domain.entities.job import Job
from domain.entities.user import User


class JobRepository(ABC):
    @abstractclassmethod
    def get_by_user(self, user: User) -> list[Job]:
        raise (NotImplementedError)
