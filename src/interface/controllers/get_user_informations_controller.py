import json

from application.repos.user_repository import UserRepository
from application.usecases.get_user_informations_usecase import \
    GetUserInformationsUsecase
from domain.entities.user import User
from domain.entities.user_informations import UserInformations


class GetUserInformationsController:
    def __init__(self, user_repository: UserRepository):
        self.get_user_informations_usecase = GetUserInformationsUsecase(
            user_repository
        )

    def format_response(self, information: UserInformations) -> str:
        address_dict = information.address.__dict__
        information.address = address_dict

        return json.dumps(information.__dict__)

    def execute(self,
                username: str,
                email: str,
                password: str,
                security_answer: str
                ) -> str:
        user = User(username, email, password, security_answer)

        user_informations = self.get_user_informations_usecase.perform(
            user
        )

        return self.format_response(user_informations)
