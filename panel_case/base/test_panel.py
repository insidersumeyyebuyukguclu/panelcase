from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pages")))

# Import page objects
from logIn_page import LogIn
from create import CreateCampaign
from make_changes import MakeChanges
from control import ControlTest

# ChromeDriver'ı kur ve başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Ana sayfaya git
driver.get("https://seleniumautomation.inone.useinsider.com/")

# 1. LogIn işlemi
login_page = LogIn(driver)
login_page.login()

# 2. Kampanya oluşturma işlemi
create_campaign_page = CreateCampaign(driver)
create_campaign_page.createCamp()

# 3. Değişiklik yapma işlemi
make_changes_page = MakeChanges(driver)
make_changes_page.changeset()

# 4. Kontrol testi
control_test_page = ControlTest(driver)
control_test_page.details()
control_test_page.settings_and_generate()
control_test_page.test_link_and_visibility()


