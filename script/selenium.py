import os
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class QiitaAutoLogin(object):
    # WebDriver のオプションを設定する
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--headless')
    # r"https://127.0.0.1:5000/"
    REDIRECT_URL = repr(os.environ.get("qiita_redirect_url"))

    def __init__(self):
        print('connectiong to remote browser...')
        self.driver = webdriver.Chrome(options=OPTIONS)

    def qiita_login_by_google_account(self):
        login_url = "https://qiita.com/login"
        self.driver.get(login_url)
        google_auth_elm = self.driver.find_element_by_class_name("btn-google-inverse")
        google_auth_elm.click()

        google_login = LinkGoogleAccountsLogin()
        google_login.auto_login(base_url)

    def quit_driver(self):
        # ブラウザを終了する
        self.driver.quit()

class LinkGoogleAccountsLogin(QiitaAutoLogin):
    EMAIL = os.environ.get("google_email")
    PASSWORD = os.environ.get("google_password")

    def __init__(self):
        super().__init__()

    def auto_login(self, redirect_url):
        self.email_input(wait_time=10)
        self.password_input(wait_time=20)
        # if completed input, called google two factor auth. Maybe, tap your smart phone
        redirect_url = "https://qiita.com/"
        self.google_login_wait(redirect_url, wait_time=30)

    def email_input(self, wait_time=10):
        expected_btn_xpath = '//*[@id="identifierNext"]'
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, expected_btn_xpath)))
        self.driver.find_element_by_tag_name("input").send_keys(self.EMAIL)
        self.driver.find_element_by_xpath(expected_btn_xpath).click()

    def password_input(self, wait_time=10):
        expected_btn_xpath = '//*[@id="passwordNext"]'
        input_pw_xpath = '//input[@name="password"]'
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, expected_btn_xpath)))
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, input_pw_xpath)))
        self.driver.find_element_by_xpath(input_pw_xpath).send_keys(self.PASSWORD)
        self.driver.find_element_by_xpath(expected_btn_xpath).click()

    def google_login_wait(self, redirect_url, wait_time=10):
        WebDriverWait(driver, wait_time).until(EC.url_matches(redirect_url))
        print(f"redirected to: {self.driver.current_url}")

class PassQiitaOAuth2(QiitaAutoLogin):

    def __init__(self):
        super().__init__()

    def passed_oauth(self):
        url = self.access_authorization()
        self.accept_oauth(url)

    def access_authorization(self):
        authorization_url, headers, body = oauth.prepare_authorization_request(
            auth_url,
            redirect_url=self.REDIRECT_URL,
            scope = scope
        )
        return authorization_url

    def accept_oauth(self, authorization_url, wait_time=10):
        self.driver.get(authorization_url)
        print(self.driver.current_url)

        accept_btn_xpath = '//input[@name="commit"]'
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, accept_btn_xpath)))
        self.driver.find_element_by_xpath(accept_btn_xpath).click()

        print(self.driver.current_url)
        print(self.driver.title)

if __name__ == "__main__":
    qal = QiitaAutoLogin()
