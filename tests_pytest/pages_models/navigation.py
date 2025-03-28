from playwright.sync_api import Page

class navigation:
    def __init__(self, page:Page):
        self.page = page

    def go_to_home(self):
        self.page.goto("https://www.arpeely.com/")

    def nav_to_about_us(self):
        self.page.click('#comp-kk2odyr61label')
        self.page.wait_for_selector('h1')

    def nav_to_contact(self):
        self.page.click('#comp-kk2odyr65label')
        self.page.wait_for_selector('h1')
    
    def get_title(self):
        return self.page.title()
