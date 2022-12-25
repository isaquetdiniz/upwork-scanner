from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

login_email = 'bobbybackupy'
login_password = 'Argyleawesome123!'
login_security_answer = 'TheDude'

login_url = "https://upwork.com/ab/account-security/login"
login_username_input_id = 'login_username'
login_password_input_id = 'login_password'
login_answer_input_id = 'login_answer'
login_six_digit_code_input_id = 'login_otp'
login_six_digit_code_otp_input_id = 'deviceAuthOtp_otp'
login_first_button_id = 'login_password_continue'
login_second_button_id = 'login_control_continue'
principal_page_url = 'https://www.upwork.com/nx/find-work/best-matches'
best_matches_class = 'up-card-section.up-card-list-section'

wait_element_seconds = 3


def get_tags(list, length):
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


def format_informations(text):
    text_splited = text.split('\n')

    length = len(text_splited)

    title = text_splited[0]
    informations = text_splited[3]
    description = text_splited[4]
    rating = text_splited[length - 4]
    salary = text_splited[length - 3]
    country = text_splited[length - 1]
    tags = get_tags(text_splited, length)

    return f'{title}, {informations}, {description}, {rating}, {salary}, {country} {tags}\n'


service = ChromeService(ChromeDriverManager(
    chrome_type=ChromeType.CHROMIUM).install())

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, wait_element_seconds)

driver.get(login_url)

email_input = wait.until(EC.element_to_be_clickable(
    (By.ID, login_username_input_id)))

email_input.clear()
email_input.send_keys(login_email)


login_first_continue_button = wait.until(
    EC.element_to_be_clickable((By.ID, login_first_button_id)))

login_first_continue_button.click()


password_input = wait.until(
    EC.element_to_be_clickable((By.ID, login_password_input_id)))

password_input.clear()
password_input.send_keys(login_password)

login_second_continue_button = wait.until(
    EC.element_to_be_clickable((By.ID, login_second_button_id)))

login_second_continue_button.click()

try:
    answer_input = wait.until(
        EC.element_to_be_clickable((By.ID, login_answer_input_id)))

    if answer_input:
        print('Need secret answer')

        answer_input.clear()
        answer_input.send_keys(login_security_answer)

        login_third_continue_button = wait.until(
            EC.element_to_be_clickable((By.ID, login_second_button_id)))

        login_third_continue_button.click()

        try:
            need_six_digit_code = wait.until(EC.element_to_be_clickable(
                (By.ID, login_six_digit_code_input_id)))

            if need_six_digit_code:
                print('Need six digit verification code')
        except:
            try:
                best_matches = wait.until(
                    EC.url_matches(principal_page_url))

                if best_matches:
                    print('Logged with success!')
            except:
                print('Login error')
except:
    print('No need secret answer')

    try:
        otp_input = wait.until(EC.element_to_be_clickable(
            By.ID, login_six_digit_code_otp_input_id))

        if otp_input:
            print('Need six digit otp verification code')
    except:
        try:
            is_in_best_matches = wait.until(
                EC.url_matches(principal_page_url))

            if is_in_best_matches:
                print('Logged with success!')

            best_matches = driver.find_elements(
                By.CLASS_NAME, best_matches_class)

            for best_match in best_matches:
                best_match_informations = best_match.get_attribute('innerText')
                print(format_informations(best_match_informations))
        except Exception as error:
            print('Login error')
            print(error)
