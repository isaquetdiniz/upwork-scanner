import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from application.repos.user_repository import UserRepository
from domain.entities.address import Address
from domain.entities.user import User
from domain.entities.user_informations import UserInformations


class SeleniumUserRepository(UserRepository):
    def __init__(self,
                 driver,
                 wait,
                 profile_modal_close_button_class,
                 profile_settings_text,
                 profile_anwser_input,
                 profile_anwser_button,
                 profile_url,
                 profile_informations_class,
                 profile_image_partial_link
                 ):

        if driver:
            self.driver = driver
        else:
            self.driver = self.load_driver()

        if wait:
            self.wait = wait
        else:
            self.wait = self.load_driver(self.driver)

        self.profile_modal_close_button_class = (
            profile_modal_close_button_class
        )
        self.profile_settings_text = profile_settings_text
        self.profile_anwser_input = profile_anwser_input
        self.profile_anwser_button = profile_anwser_button
        self.profile_url = profile_url
        self.profile_informations_class = profile_informations_class
        self.profile_image_partial_link = profile_image_partial_link

    def load_driver(self):
        service = ChromeService(ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install())

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=service, options=options)

        return driver

    def load_wait(self, driver):
        wait = WebDriverWait(driver, self.wait_element_seconds)
        return wait

    def close_modal(self):
        close = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CLASS_NAME,
                    self.profile_modal_close_button_class
                )

            )
        )

        close.click()

    def go_to_settings(self):
        settings = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.LINK_TEXT,
                    self.profile_settings_text
                )
            )
        )

        settings.click()

    def need_anwser_verify(self):
        try:
            anwser_input = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        self.profile_anwser_input
                    )
                )
            )
        except Exception:
            False
        else:
            return anwser_input

    def anwser_verify(self, input, user: User):
        input.clear()
        input.send_keys(user.security_answer)

        button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CLASS_NAME,
                    self.profile_anwser_button
                )
            )
        )

        button.click()

    def is_in_profile_page(self) -> bool:
        try:
            self.wait.until(
                EC.url_matches(
                    self.profile_url
                )
            )
        except Exception:
            return False
        else:
            return True

    def get_informations(self) -> UserInformations:
        time.sleep(1)

        contact_informations = self.driver.find_elements(
            By.CLASS_NAME,
            self.profile_informations_class
        )

        informations = {}

        for i, contact_information in enumerate(contact_informations):
            contact = contact_information.get_attribute(
                'innerText'
            )

            contact_splited = contact.split('\n')

            if i == 4:
                informations[
                    contact_splited[0]
                ] = contact_splited[1:len(contact_splited)]
            else:
                informations[contact_splited[0]] = contact_splited[1]

        name_splited = informations['Name'].split(' ')

        try:
            picture = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.PARTIAL_LINK_TEXT,
                        self.profile_image_partial_link
                    )
                )
            )
        except Exception:
            picture_url = ''
        else:
            picture_url = picture.getAttribute("src")

        address = Address(
            informations['Address'][0],
            informations['Address'][1],
            informations['Address'][2],
            informations['Address'][2],
            informations['Address'][2],
            informations['Address'][3]

        )

        user_informations = UserInformations(
            informations['User ID'],
            name_splited[0],
            name_splited[len(name_splited) - 1],
            informations['Name'],
            informations['Email'],
            informations['Phone'],
            picture_url,
            address
        )

        return user_informations

    def get_informations_by_user(self, user: User) -> UserInformations:
        self.close_modal()
        self.go_to_settings()

        if self.is_in_profile_page():
            print('Profile page')
            return self.get_informations()

        anwser_input = self.need_anwser_verify()
        if anwser_input:
            print('Need anwser verify')
            self.anwser_verify(anwser_input, user)

            if self.is_in_profile_page():
                print('Profile page')
                return self.get_informations()

            return UserInformations()

        return UserInformations()
