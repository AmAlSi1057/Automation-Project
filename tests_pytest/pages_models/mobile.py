from playwright.sync_api import Page

class mobile:
    def __init__(self, page: Page):
        self.page = page

    def set_viewport(self, device):
        mobile = self.page.context().devices[device]
        self.page.set_viewport_size({
            "width": mobile["viewport"]["width"],
            "height": mobile["viewport"]["height"]})
        
    def mobile_menu(self):
        self.page.locator('button[aria-label="Open menu"]')

    def mobile_home(self):
        self.page.goto("https://www.arpeely.com/")