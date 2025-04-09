from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class ControlTestLocators:
    DETAILS_BUTTON = (By.CSS_SELECTOR, '.is-button.button.d-f.cur-p.h-4-s')
    PRIORITY_VALUE = (By.ID, "priority-value")
    ELEMENT_TEXT = (By.CSS_SELECTOR, '.f-s-2.t-c-2.w-b-b-w.personalization-rule-0')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '.in-modal-wrapper__icon.qa-close.ml-2')
    SETTINGS_LINK = (By.CSS_SELECTOR, '.in-header-wrapper__links.router-link-exact-active.router-link-active')
    GENERATE_BUTTON = (By.XPATH, "//a[text()='Generate']")
    TEST_LINK_BUTTON = (By.CSS_SELECTOR, '.is-test-link.test-link.d-f.cur-p.p-r.h-4-s')
    ICON_CHEVRON = (By.CSS_SELECTOR, '.icon.qa-icon.ml-2.fl-r.i-c-2.line-chevron-small-right')
    LINK_OPTION = (By.CSS_SELECTOR, '.clearfix.w-1.option__child.option__0-child.option_active-child')
    VISIBILITY_ELEMENT = (By.CLASS_NAME, 'inspector-personalization-visibility')

class ControlTest:
    def __init__(self, driver):
        self.driver = driver

    def details(self):
        wait = WebDriverWait(self.driver, 10)
        
        # Click on details button
        details_element = wait.until(EC.element_to_be_clickable(ControlTestLocators.DETAILS_BUTTON))
        details_element.click()

        # Verify priority value
        priority_element = wait.until(EC.element_to_be_clickable(ControlTestLocators.PRIORITY_VALUE))
        priority_value = priority_element.text
        assert priority_value == "3", f"Expected 3, but got {priority_value}"

        # Verify element text
        element = self.driver.find_element(*ControlTestLocators.ELEMENT_TEXT)
        element_text = element.text.strip()
        assert element_text == "Page Type is All Pages", f"Expected 'Page Type is All Pages', but got '{element_text}'"

        # Close the modal
        close_button = self.driver.find_element(*ControlTestLocators.CLOSE_BUTTON)
        close_button.click()

    def settings_and_generate(self):
        # Navigate to settings
        settings = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ControlTestLocators.SETTINGS_LINK))
        settings.click()
        time.sleep(5)  # wait for campaign set
        
        # Click on 'Generate'
        generate_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ControlTestLocators.GENERATE_BUTTON))
        generate_element.click()

        time.sleep(10)  # wait for generate time
        self.driver.refresh()

        # Click settings again and 'Generate'
        settings = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ControlTestLocators.SETTINGS_LINK))
        settings.click()
        time.sleep(15)  # wait for campaign set
        
        generate_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ControlTestLocators.GENERATE_BUTTON))
        generate_element.click()

    def test_link_and_visibility(self):
        # Click on the test link
        test_link_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ControlTestLocators.TEST_LINK_BUTTON))
        test_link_element.click()

        # Move to the chevron icon
        element2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ControlTestLocators.ICON_CHEVRON))
        action = ActionChains(self.driver)
        action.move_to_element(element2).perform()

        # Click on the link option
        link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ControlTestLocators.LINK_OPTION))
        link.click()

        # Check if visibility element is present
        visibility_element = None
        try:
            visibility_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ControlTestLocators.VISIBILITY_ELEMENT))
        except TimeoutException:
            pass
        
        if visibility_element and visibility_element.is_displayed():
            print("Element is visible and found!")
        else:
            print("Assertion Error: Kampanya visible değil")
