import json
from application.repos.job_repository import JobRepository
from application.usecases.get_user_jobs_usecase import GetUserJobsUsecase
from domain.entities.job import Job
from domain.entities.user import User


class GetUserJobsController:
    def __init__(self, job_repository: JobRepository):
        self.get_user_jobs_usecase = GetUserJobsUsecase(job_repository)


    def tranform_to_json(self, job: Job) -> str:
        return json.dumps(job.__dict__)

    def format_response(self, jobs: list[Job]) -> str:
        jobs_json = []

        for job in jobs:
            job_to_json = self.tranform_to_json(job)
            jobs_json.append(job_to_json)

        return json.dumps({"jobs": jobs_json })


    def execute(self, username: str, email: str, password: str, security_answer: str) -> str:
        user = User(username, email, password, security_answer)

        jobs = self.get_user_jobs_usecase.perform(user)

        return self.format_response(jobs)

