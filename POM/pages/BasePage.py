from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """Click on a visible element."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """Enter text into an input field."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        """Retrieve and return text of a visible element."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_visible(self, by_locator):
        """Check if an element is visible."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, by_locator):
        """Check if an element is present in the DOM."""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_title(self):
        """Retrieve the title of the current page."""
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        """Retrieve a specific attribute value of an element."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def do_clear(self, by_locator):
        """Clear the text of an input field."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def wait_for_element_to_be_clickable(self, by_locator):
        """Wait until an element is clickable."""
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))

    def scroll_to_element(self, by_locator):
        """Scroll to a specific element on the page."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_alert_and_accept(self):
        """Wait for an alert and accept it."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present()).accept()

    def switch_to_frame(self, by_locator):
        """Switch to an iframe using a locator."""
        iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        """Switch back to the default content from an iframe."""
        self.driver.switch_to.default_content()

    def take_screenshot(self, file_path):
        """Take a screenshot and save it to the specified file path."""
        self.driver.save_screenshot(file_path)

    def hover_over_element(self, by_locator):
        """Hover over an element."""
        from selenium.webdriver.common.action_chains import ActionChains
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
