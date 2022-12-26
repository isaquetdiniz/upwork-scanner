import json
from application.repos.job_repository import JobRepository
from application.usecases.get_user_jobs_usecase import GetUserJobsUsecase
from domain.entities.job import Job
from domain.entities.user import User


class GetUserJobsController:
    def __init__(self, job_repository: JobRepository):
        self.get_user_jobs_usecase = GetUserJobsUsecase(job_repository)

    def format_response(self, jobs: list[Job]) -> str:
        jobs_dict = []

        for job in jobs:
            client_dict = job.client.__dict__
            job.client = client_dict

            job_dict = job.__dict__

            jobs_dict.append(job_dict)

        return json.dumps({"jobs": jobs_dict })


    def execute(self, username: str, email: str, password: str, security_answer: str) -> str:
        user = User(username, email, password, security_answer)

        jobs = self.get_user_jobs_usecase.perform(user)

        return self.format_response(jobs)

