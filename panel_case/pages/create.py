from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CreateCampaignLocators:
    # Sayfa elemanlarının locators
    CAMPAIGN_NAME = (By.ID, "campaign-name")
    ACCEPT_BUTTON = (By.ID, "accept")
    SAVE_AND_NEXT_BUTTON = (By.ID, "save-and-next")
    RULES_ELEMENT = (By.CSS_SELECTOR, "a[data-v-3b7dc63c]")
    CONDITION_LIST_ITEM = (By.ID, "conditionList0")
    PAGE_TYPE_OPTION = (By.CSS_SELECTOR, ".option__2.conditionList0-page-type")
    ADD_VARIANT_BUTTON = (By.ID, "add-new-variation")
    FIRST_LIST_ITEM = (By.CLASS_NAME, "btn-select")
    OK_BUTTON = (By.XPATH, '//div[@id="inline-select-notification"]//a[.="OK"]')
    IFRAME = (By.ID, 'ins-skeleton-partner-iframe')
    SELECT_ELEMENT = (By.XPATH, '//div[@class="top-header"]/div[@class="wrap"]')
    AFTER_ELEMENT = (By.CLASS_NAME, 'append-after')
    SAVE_BUTTON = (By.ID, "save")
    LAUNCH_BUTTON = (By.XPATH, "//a[contains(@href, '/launch')]")


class CreateCampaign:
    def __init__(self, driver):
        self.driver = driver

    def create_campaign(self):
        # Kampanya adı girme
        campaign_name_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.CAMPAIGN_NAME)
        )
        campaign_name_element.click()
        campaign_name_element.send_keys("test")

        # Kabul butonuna tıklama
        accept_button = self.driver.find_element(*CreateCampaignLocators.ACCEPT_BUTTON)
        accept_button.click()

        # "Save and Next" butonuna tıklama
        rules = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.SAVE_AND_NEXT_BUTTON)
        )
        rules.click()

        time.sleep(5)

        # Kurallar seçme
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.RULES_ELEMENT)
        )
        element.click()

        # Koşul listesine tıklama
        element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CreateCampaignLocators.CONDITION_LIST_ITEM)
        )
        element2.click()

        # Page Type seçme
        element3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CreateCampaignLocators.PAGE_TYPE_OPTION)
        )
        element3.click()

        # Tasarım adımına geçiş
        design = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.SAVE_AND_NEXT_BUTTON)
        )
        design.click()

        # Yeni varyasyon ekleme
        add_variant = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.ADD_VARIANT_BUTTON)
        )
        add_variant.click()

        time.sleep(3)

        # İlk liste öğesine tıklama
        first_list_item = self.driver.find_element(*CreateCampaignLocators.FIRST_LIST_ITEM)
        first_list_item.click()

        time.sleep(15)

        # "OK" butonuna tıklama
        ok_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.OK_BUTTON)
        )
        ok_button.click()

        # Iframe'e geçiş
        iframe = WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(CreateCampaignLocators.IFRAME)
        )

        # İlk öğeye tıklama
        select_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.SELECT_ELEMENT)
        )
        select_element.click()

        # Iframe'den çıkma
        self.driver.switch_to.default_content()

        # "After Save" elementine tıklama
        after_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.AFTER_ELEMENT)
        )
        after_element.click()

        # Kampanyayı kaydetme
        after_save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.SAVE_BUTTON)
        )
        after_save.click()

        # Kampanyayı başlatma
        launch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateCampaignLocators.LAUNCH_BUTTON)
        )
        launch.click()
