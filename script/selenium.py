import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
#options.add_argument('--headless')

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

driver.get("https://qiita.com/login")
elm = driver.find_element_by_class_name("btn-google-inverse")
elm.click()
print(elm)

wait_time = 10
login_id_xpath = '//*[@id="identifierNext"]'
WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
driver.find_element_by_tag_name("input").send_keys("nakaka33@gmail.com")
driver.find_element_by_xpath(login_id_xpath).click()

login_pw_xpath = '//*[@id="passwordNext"]'
WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
driver.find_element_by_xpath('//input[@name="password"]').send_keys("naka3465")
driver.find_element_by_xpath(login_pw_xpath).click()

WebDriverWait(driver, wait_time+10).until(EC.url_matches("https://qiita.com/"))
print("qiita")

authorization_url, headers, body = oauth.prepare_authorization_request(
    auth_url,
    redirect_url=r"https://127.0.0.1:5000/",
    scope = scope
)
driver.get(authorization_url)
print(driver.current_url)

accept_btn_xpath = '//input[@name="commit"]'
WebDriverWait(driver, wait_time+20).until(EC.presence_of_element_located((By.XPATH, accept_btn_xpath)))
driver.find_element_by_xpath(accept_btn_xpath).click()

print(driver.current_url)
print(driver.title)

# ブラウザを終了する
driver.quit()

redirect_url=r"https://127.0.0.1:5000/"
res = requests.get(driver.current_url)
res.read()
