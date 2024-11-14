class Button:
    def __init__(self, page, locator: str, max_time=30):
        self.page = page
        self.locator = locator
        self.max_time = max_time

    def click(self):
        self.page.locator(self.locator).click()

    def visible(self):
        return self.page.locator(self.locator).is_visible(timeout=self.max_time)
