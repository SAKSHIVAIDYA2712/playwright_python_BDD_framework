from UI_Elements import Button, TextInput


class BasePage:
    def __init__(self, context, page):
        self.context = context
        self.page = page

    def fill_input(self, locator: str, text: str):
        TextInput(self.page, locator).enter_text(text)

    def click_button(self, locator: str):
        Button(self.page, locator).click()

    def wait_for_element(self, locator: str, timeout: int = 30):
        self.page.wait_for_selector(locator, timeout=timeout)

    def is_element_visible(self, locator: str, timeout: int = 30) -> bool:
        return self.page.locator(locator).is_visible(timeout=timeout)

    def expect_navigation(self):
        self.page.goto(self.context.target_address)
