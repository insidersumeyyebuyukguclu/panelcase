from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MakeChangesLocators:
    PERSONALIZATION_LANGUAGE_BUTTON = (By.ID, "personalization-language")
    THIRD_LANGUAGE_OPTION = (By.XPATH, "(//a[contains(@class, 'personalization-language-all-languages')])")
    RADIO_BUTTON_LABEL = (By.XPATH, "//label[@for='Never Ends']")
    DISPLAY_SETTINGS = (By.CSS_SELECTOR, ".qa-accordion-wrapper.in-accordion-wrapper.clearfix")
    PRIORITY_DROPDOWN = (By.ID, "priority")
    THIRD_OPTION = (By.CSS_SELECTOR, "div[title=\"3\"]")
    TEST_LABEL = (By.XPATH, '//label[@for="Test"]')
    SAVE_AND_NEXT_BUTTON = (By.ID, "save-and-next")


class MakeChanges:
    def __init__(self, driver):
        self.driver = driver

    def changeset(self):
        # Personalization Language butonuna tıklama
        personalization_language_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MakeChangesLocators.PERSONALIZATION_LANGUAGE_BUTTON)
        )
        personalization_language_button.click()

        # Üçüncü dili seçme
        third_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MakeChangesLocators.THIRD_LANGUAGE_OPTION)
        )
        third_language.click()

        # Radio button "Never Ends" seçimi
        radio_button_label = self.driver.find_element(*MakeChangesLocators.RADIO_BUTTON_LABEL)
        radio_button_label.click()

        time.sleep(3)

        # Sayfanın en altına kaydırma
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Display settings kısmına tıklama
        display_settings = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(MakeChangesLocators.DISPLAY_SETTINGS)
        )
        display_settings[1].click()

        # Priority dropdown'ını açma
        drop_down_search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MakeChangesLocators.PRIORITY_DROPDOWN)
        )
        drop_down_search.click()

        # Üçüncü seçenekle tıklama
        third_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MakeChangesLocators.THIRD_OPTION)
        )
        third_option.click()

        # "Test" radio butonuna tıklama
        test = self.driver.find_element(*MakeChangesLocators.TEST_LABEL)
        test.click()

        # Save and Next butonuna tıklama
        launch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MakeChangesLocators.SAVE_AND_NEXT_BUTTON)
        )
        launch.click()
