from application.repos.user_repository import UserRepository
from domain.entities.user import User


class GetUserInformationsUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def perform(self, user: User):
        user_informations = self.user_repository.get_informations_by_user(
            user
        )

        return user_informations
