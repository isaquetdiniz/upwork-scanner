from dotenv import dotenv_values

class Env:
    def __init__(self):
        self.config = dotenv_values(".env")

    def load_informations(self, dict: dict[str, dict[str, str]]) -> dict[str, str]:
        informations = {}

        for key, value in dict.items():
            new_name = value['new_name']
            default = value['default']

            value = self.config[key]

            if not value and not default:
                raise Exception(f'Missing {key} in env!')
            elif not value and default:
                informations[new_name] = default
            else:
                if key == 'WAIT_ELEMENT_SECONDS':
                    informations[new_name] = int(value)
                else:
                    informations[new_name] = value

        return informations


    def load_user_informations(self) -> dict[str, str]:
        configs = {
            'LOGIN_EMAIL': { 'new_name': 'email', 'default': ''},
            'LOGIN_PASSWORD': { 'new_name': 'password', 'default': ''},
            'LOGIN_SECURITY_ANSWER': { 'new_name': 'security_anwser', 'default': ''}
        }

        return self.load_informations(configs)


    def load_scrapping_informations(self) -> dict[str, str | int]:
        configs = {
            'LOGIN_URL': { 'new_name': 'login_url', 'default': 'https://upwork.com/ab/account-security/login'},
            'LOGIN_USERNAME_INPUT_ID': { 'new_name': 'login_username_input_id', 'default': 'login_username'},
            'LOGIN_PASSWORD_INPUT_ID': { 'new_name': 'login_password_input_id', 'default': 'login_password'},
            'LOGIN_ANSWER_INPUT_ID': { 'new_name': 'login_answer_input_id', 'default': 'login_answer'},
            'LOGIN_SIX_DIGIT_CODE_INPUT_ID': { 'new_name': 'login_six_digit_code_input_id', 'default': 'login_otp'},
            'LOGIN_SIX_DIGIT_CODE_OTP_INPUT_ID': { 'new_name': 'login_six_digit_code_otp_input_id', 'default': 'deviceAuthOtp_otp'},
            'LOGIN_FIRST_BUTTON_ID': { 'new_name': 'login_first_button_id', 'default': 'login_password_continue'},
            'LOGIN_SECOND_BUTTON_ID': { 'new_name': 'login_second_button_id', 'default': 'login_control_continue'},
            'PRINCIPAL_PAGE_URL': { 'new_name': 'principal_page_url', 'default': 'https://www.upwork.com/nx/find-work/best-matches'},
            'BEST_MATCHES_CLASS': { 'new_name': 'best_matches_class', 'default': 'up-card-section.up-card-list-section'},
            'WAIT_ELEMENT_SECONDS': { 'new_name': 'wait_element_seconds', 'default': 3},
        }

        return self.load_informations(configs)