from playwright.sync_api import expect
from page_models.basepage import BasePage
from UI_Elements.dropdown import Dropdown


class FormPage(BasePage):
    def __init__(self, context, page):
        super().__init__(context, page)

        self.username_locator = 'input[id="fullName"]'
        self.email_locator = 'input[id="email"]'
        self.gender_locator = 'select[id="gender"]'
        self.dob_locator = 'input[id="dob"]'
        self.address_locator = 'input[id="address"]'
        self.submit_button_locator = 'button[type="submit"]'
        self.success_message_locator = 'span[id="success"]'
        self.error_messages_locators = {
            'name': 'text="Please enter your full name"',
            'email': 'text="Please enter your email address"',
            'gender': 'text="Please select a gender"',
            'dob': 'text="Please select your date of birth"',
            'address': 'text="Please enter your address"',
        }

    def enter_username(self, username: str):
        self.fill_input(self.username_locator, username)

    def enter_email(self, email: str):
        self.fill_input(self.email_locator, email)

    def select_gender(self, gender: str):
        Dropdown(self.page, self.gender_locator).select_option(gender)
        # select_element = self.page.locator(self.gender_locator)
        # select_element.select_option(label=gender)

    def enter_dob(self, dob: str):
        self.fill_input(self.dob_locator, dob)

    def enter_address(self, address: str):
        self.fill_input(self.address_locator, address)

    def submit_form(self):
        self.click_button(self.submit_button_locator)

    def verify_success_message(self):
        print("I am here")
        try:
            expect(self.page.locator(self.success_message_locator)).to_be_visible(timeout="40000")
            print("success message displayed")
            return True
        except:
            print("Success message not found")
            self.check_for_validation_errors()
            return False

    def check_for_validation_errors(self):
        for field, error_locator in self.error_messages_locators.items():
            if self.page.is_visible(error_locator, timeout="40000"):
                print(f"Validation error found for {field}")
            else:
                print(f"No validation error for {field}")

    def fill_and_submit_form(self, username: str, email: str, gender: str, dob: str, address: str, context):
        self.enter_username(username)
        self.enter_email(email)
        self.select_gender(gender)
        self.enter_dob(dob)
        self.enter_address(address)
        self.submit_form()
