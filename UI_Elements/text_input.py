class TextInput:
    def __init__(self, page, locator: str):
        self.page = page
        self.locator = locator

    def enter_text(self, text: str):
        self.page.fill(self.locator, text)
