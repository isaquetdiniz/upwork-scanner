from infra.dotenv.env import Env
from infra.selenium.selenium_job_repository import SeleniumJobRepository
from infra.selenium.selenium_user_repository import SeleniumUserRepository
from interface.controllers.get_user_informations_controller import \
    GetUserInformationsController
from interface.controllers.get_user_jobs_controller import \
    GetUserJobsController

env = Env()

user_informations = env.load_user_informations()
scrapping_informations = env.load_scrapping_informations()

selenium_job_repository = SeleniumJobRepository(
    scrapping_informations['login_url'],
    scrapping_informations['login_username_input_id'],
    scrapping_informations['login_password_input_id'],
    scrapping_informations['login_answer_input_id'],
    scrapping_informations['login_six_digit_code_input_id'],
    scrapping_informations['login_six_digit_code_otp_input_id'],
    scrapping_informations['login_first_button_id'],
    scrapping_informations['login_second_button_id'],
    scrapping_informations['principal_page_url'],
    scrapping_informations['best_matches_class'],
    scrapping_informations['wait_element_seconds']
)

get_user_jobs_controller = GetUserJobsController(selenium_job_repository)

jobs_json = get_user_jobs_controller.execute(
    '',
    user_informations['email'],
    user_informations['password'],
    user_informations['security_anwser']
)

with open("jobs.json", 'w') as file:
    file.write(jobs_json)

selenium_user_repository = SeleniumUserRepository(
    selenium_job_repository.driver,
    selenium_job_repository.wait,
    scrapping_informations['profile_modal_close_button_class'],
    scrapping_informations['profile_settings_text'],
    scrapping_informations['profile_anwser_input'],
    scrapping_informations['profile_anwser_button'],
    scrapping_informations['profile_url'],
    scrapping_informations['profile_informations_class'],
    scrapping_informations['profile_image_partial_link']
)

get_user_informations_controller = GetUserInformationsController(
    selenium_user_repository)

informations = get_user_informations_controller.execute(
    '',
    user_informations['email'],
    user_informations['password'],
    user_informations['security_anwser']
)

with open("user_informations.json", 'w') as file:
    file.write(informations)
