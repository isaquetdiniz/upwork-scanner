import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from application.repos.job_repository import JobRepository
from domain.entities.client import Client
from domain.entities.job import Job
from domain.entities.user import User


class SeleniumJobRepository(JobRepository):
    def __init__(self,
                 login_url: str,
                 login_username_input_id: str,
                 login_password_input_id: str,
                 login_answer_input_id: str,
                 login_six_digit_code_input_id: str,
                 login_six_digit_code_otp_input_id: str,
                 login_first_button_id: str,
                 login_second_button_id: str,
                 principal_page_url: str,
                 best_matches_class: str,
                 wait_element_seconds: int
                 ):
        self.login_url = login_url
        self.login_username_input_id = login_username_input_id
        self.login_password_input_id = login_password_input_id
        self.login_answer_input_id = login_answer_input_id
        self.login_six_digit_code_input_id = login_six_digit_code_input_id
        self.login_six_digit_code_otp_input_id = login_six_digit_code_otp_input_id
        self.login_first_button_id = login_first_button_id
        self.login_second_button_id = login_second_button_id
        self.principal_page_url = principal_page_url
        self.best_matches_class = best_matches_class
        self.wait_element_seconds = wait_element_seconds

    def get_tags(self, list: list[str], length: int) -> list[str]:
        tags = []

        position_first_tag = 5

        first_tag = list[position_first_tag]

        if first_tag.find('more') != -1:
            position_first_tag = 7

        for i in range(position_first_tag, length - 8):
            tag = list[i]

            if tag != 'Next skills':
                tags.append(list[i])

        return tags

    def transform_to_job(self, text: str) -> Job:
        text_splited = text.split('\n')

        length = len(text_splited)

        title = text_splited[0]

        informations = text_splited[3]
        informations_splited = informations.split(' - ')

        level = informations_splited[1]

        payment = informations_splited[0] + ' ' + informations_splited[2]

        description = text_splited[4]

        rating = text_splited[length - 4]
        rating_formatted = re.sub("[A-z]|\s", "", rating)[:-1]
        rating_float = float(rating_formatted)

        spent = text_splited[length - 3]
        spent_formatted = re.sub(
            "\s|spent|\+",
            "",
            spent
        ).replace('k', ',000')

        country = text_splited[length - 1]

        tags = self.get_tags(text_splited, length)

        client = Client(
            rating_float,
            spent_formatted,
            country
        )

        job = Job(
            title,
            description,
            tags,
            level,
            payment,
            client
        )

        return job

    def get_by_user(self, user: User) -> list[Job]:
        service = ChromeService(ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install())

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=service, options=options)

        wait = WebDriverWait(driver, self.wait_element_seconds)

        driver.get(self.login_url)

        email_input = wait.until(EC.element_to_be_clickable(
            (By.ID, self.login_username_input_id)))

        email_input.clear()
        email_input.send_keys(user.email)

        login_first_continue_button = wait.until(
            EC.element_to_be_clickable((By.ID, self.login_first_button_id)))

        login_first_continue_button.click()

        password_input = wait.until(
            EC.element_to_be_clickable((By.ID, self.login_password_input_id)))

        password_input.clear()
        password_input.send_keys(user.password)

        login_second_continue_button = wait.until(
            EC.element_to_be_clickable((By.ID, self.login_second_button_id)))

        login_second_continue_button.click()

        try:
            answer_input = wait.until(
                EC.element_to_be_clickable((By.ID, self.login_answer_input_id)))

            if answer_input:
                print('Need secret answer')

                answer_input.clear()
                answer_input.send_keys(user.security_answer)

                login_third_continue_button = wait.until(
                    EC.element_to_be_clickable((By.ID, self.login_second_button_id)))

                login_third_continue_button.click()

                try:
                    need_six_digit_code = wait.until(EC.element_to_be_clickable(
                        (By.ID, self.login_six_digit_code_input_id)))

                    if need_six_digit_code:
                        print('Need six digit verification code')
                except:
                    try:
                        is_in_best_matches = wait.until(
                            EC.url_matches(self.principal_page_url))

                        if is_in_best_matches:
                            print('Logged with success!')

                        best_matches = driver.find_elements(
                            By.CLASS_NAME, self.best_matches_class)

                        best_matches_jobs: list[Job] = []

                        for best_match in best_matches:
                            best_match_informations = best_match.get_attribute(
                                'innerText')
                            job = self.transform_to_job(
                                best_match_informations)
                            best_matches_jobs.append(job)

                        return best_matches_jobs
                    except:
                        print('Login error')
        except:
            print('No need secret answer')

            try:
                otp_input = wait.until(EC.element_to_be_clickable(
                    By.ID, self.login_six_digit_code_otp_input_id))

                if otp_input:
                    print('Need six digit otp verification code')
            except:
                try:
                    is_in_best_matches = wait.until(
                        EC.url_matches(self.principal_page_url))

                    if is_in_best_matches:
                        print('Logged with success!')

                    best_matches = driver.find_elements(
                        By.CLASS_NAME, self.best_matches_class)

                    best_matches_jobs: list[Job] = []

                    for best_match in best_matches:
                        best_match_informations = best_match.get_attribute(
                            'innerText')
                        job = self.transform_to_job(best_match_informations)
                        best_matches_jobs.append(job)

                    return best_matches_jobs
                except Exception as error:
                    print('Login error')
                    print(error)
