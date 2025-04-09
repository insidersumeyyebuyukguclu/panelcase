from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogInLocators:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    CREATE_MOBILE_CAMPAIGN_BUTTON = (By.ID, 'create-mobile-campaign')

class LogIn:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        # E-posta alanına tıklayıp e-posta adresini girme
        email_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LogInLocators.EMAIL_FIELD)
        )
        email_area.click()
        email_area.send_keys("sumeyye.buyukguclu@useinsider.com")

        # Şifre alanına şifreyi girme
        password_area = self.driver.find_element(*LogInLocators.PASSWORD_FIELD)
        password_area.send_keys("")  # Buraya şifreyi girin

        # Giriş butonuna tıklama
        login_button = self.driver.find_element(*LogInLocators.LOGIN_BUTTON)
        login_button.click()

        # Sayfanın yüklenmesini bekleme
        time.sleep(10)

        # Belirtilen URL'ye gitme
        self.driver.get("https://seleniumautomation.inone.useinsider.com/instory-all")

        # Mobil kampanya oluşturma butonuna tıklama
        create_campaign_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LogInLocators.CREATE_MOBILE_CAMPAIGN_BUTTON)
        )
        create_campaign_button.click()

        # Sayfa yüklenmesini bekleme
        time.sleep(5)
