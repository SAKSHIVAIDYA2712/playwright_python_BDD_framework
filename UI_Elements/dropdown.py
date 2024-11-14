class Dropdown:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def select_option(self, label):
        select_element = self.page.locator(self.locator)
        select_element.select_option(label=label)
