from abc import ABC, abstractclassmethod

from domain.entities.user import User
from domain.entities.user_informations import UserInformations


class UserRepository(ABC):
    @abstractclassmethod
    def get_informations_by_user(self, user: User) -> UserInformations:
        raise (NotImplementedError)
