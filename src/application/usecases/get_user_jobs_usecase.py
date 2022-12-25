from domain.entities.user import User
from src.application.repos.job_repository import JobRepository

class GetUserJobsUsecase:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def perform(self, user: User):
        jobs = self.job_repository.get_by_user()

        return jobs
