import time
from locust import constant, events, run_single_user, task
from locust_plugins.users.webdriver import WebdriverUser
from locust_plugins.listeners import RescheduleTaskOnFail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TriangleApplicationUser(WebdriverUser):
    host = "https://testpages.eviltester.com"

    wait_time = constant(2)
    # webdriver client options can be customized by overriding the option_args
    option_args = [
        "--disable-translate",
        "--disable-extensions",
        "--disable-background-networking",
        "--safebrowsing-disable-auto-update",
        "--disable-sync",
        "--metrics-recording-only",
        "--disable-default-apps",
        "--no-first-run",
        "--disable-setuid-sandbox",
        "--hide-scrollbars",
        "--no-sandbox",
        "--no-zygote",
        "--autoplay-policy=no-user-gesture-required",
        "--disable-notifications",
        "--disable-logging",
        "--disable-permissions-api",
        "--ignore-certificate-errors",
    ]

    if __name__ == "__main__":
        # wait a bit at the end to make debugging easier
        wait_time = constant(5)
    else:
        # headless by default if running real locust and not just debugging
        headless = True

    def on_start(self):
        self.client.set_window_size(1400, 1000)
        self.client.implicitly_wait(5)

    @task
    def equilateral_triangle_page(self):
        self.clear()
        self.client.start_time = time.monotonic()  # to measure the time from now to first locust_find_element finishes
        # scenario_start_time = self.client.start_time  # to measure the time for the whole scenario
        self.client.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")

        side1_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side1", name="Side 1 = 599")
        side1_input.click()
        side1_input.send_keys("599")

        side2_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side2", name="Side 2 = 599")
        side2_input.click()
        side2_input.send_keys("599")

        side3_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side3", name="Side 3 = 599")
        side3_input.click()
        side3_input.send_keys("599")

        side3_input.send_keys(Keys.RETURN)
        self.client.implicitly_wait(10)

        answer_text = self.client.locust_find_element(By.CSS_SELECTOR, "#triangle-type", name="Equilateral")
        assert answer_text.text == 'Equilateral'

    @task
    def isosceles_triangle_page(self):
        self.clear()
        self.client.start_time = time.monotonic()  # to measure the time from now to first locust_find_element finishes
        # scenario_start_time = self.client.start_time  # to measure the time for the whole scenario
        self.client.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")

        side1_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side1", name="Side 1 = 311")
        side1_input.click()
        side1_input.send_keys("311")

        side2_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side2", name="Side 2 = 419")
        side2_input.click()
        side2_input.send_keys("419")

        side3_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side3", name="Side 3 = 311")
        side3_input.click()
        side3_input.send_keys("311")

        side3_input.send_keys(Keys.RETURN)
        self.client.implicitly_wait(10)

        answer_text = self.client.locust_find_element(By.CSS_SELECTOR, "#triangle-type", name="Isosceles")
        assert answer_text.text == 'Isosceles'

    @task
    def scalene_triangle_page(self):
        self.clear()
        self.client.start_time = time.monotonic()  # to measure the time from now to first locust_find_element finishes
        # scenario_start_time = self.client.start_time  # to measure the time for the whole scenario
        self.client.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")

        side1_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side1", name="Side 1 = 3")
        side1_input.click()
        side1_input.send_keys("3")

        side2_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side2", name="Side 2 = 4")
        side2_input.click()
        side2_input.send_keys("4")

        side3_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side3", name="Side 3 = 5")
        side3_input.click()
        side3_input.send_keys("5")

        side3_input.send_keys(Keys.RETURN)
        self.client.implicitly_wait(10)

        answer_text = self.client.locust_find_element(By.CSS_SELECTOR, "#triangle-type", name="Scalene")
        assert answer_text.text == 'Scalene'

    @task
    def not_a_triangle_page(self):
        self.clear()
        self.client.start_time = time.monotonic()  # to measure the time from now to first locust_find_element finishes
        # scenario_start_time = self.client.start_time  # to measure the time for the whole scenario
        self.client.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")

        side1_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side1", name="Side 1 = 1187")
        side1_input.click()
        side1_input.send_keys("1187")

        side2_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side2", name="Side 2 = 1319")
        side2_input.click()
        side2_input.send_keys("1319")

        side3_input = self.client.locust_find_element(By.CSS_SELECTOR, "#side3", name="Side 3 = 79")
        side3_input.click()
        side3_input.send_keys("79")

        side3_input.send_keys(Keys.RETURN)
        self.client.implicitly_wait(10)

        answer_text = self.client.locust_find_element(By.CSS_SELECTOR, "#triangle-type", name="Error: Not a Triangle")
        assert answer_text.text == 'Error: Not a Triangle'


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    RescheduleTaskOnFail(environment)


# if launched directly, e.g. "python tests/triangle_application.py", not "locust -f tests/triangle_application.py"
# This allows for `breakpoint()` for debugging
if __name__ == "__main__":
    run_single_user(TriangleApplicationUser)
