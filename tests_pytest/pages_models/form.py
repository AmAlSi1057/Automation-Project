from playwright.sync_api import Page

class form:
    def __init__(self, page:Page):
        self.page = page

    def goto_contact(self):
        self.page.goto("https://www.arpeely.com/contact")

    def empty_submit(self):
        self.page.click('button[aria-label="Submit"]')

    def fill_and_submit(self, name, message, email):
        self.page.fill('input[name="name"]', name)
        self.page.fill('id="textarea_comp-kzzez81j""]', message)
        self.page.fill('input[name="email"]', email)
        self.page.click('button[aria-label="Submit"]')

    def fill_and_submit_noemail(self, name, message):
        self.page.fill('input[name="name"]', name)
        self.page.fill('textarea[id="textarea_comp-kzzez81j"]', message)
        self.page.click('button[aria-label="Submit"]')

    def fill_and_submit_justemail(self, email):
        self.page.fill('input[name="email"]', email)
        self.page.click('button[aria-label="Submit"]')

    def get_error(self):
        self.page.locator('.error-message').text_content()

    def get_success(self):
        self.page.locator('.success-message').text_content()
        