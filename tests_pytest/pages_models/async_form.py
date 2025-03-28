from playwright.async_api import Page

class form:
    def __init__(self, page:Page):
        self.page = page

    async def goto_contact(self):
        await self.page.goto("https://www.arpeely.com/contact")

    async def empty_submit(self):
        await self.page.click('button[aria-label="Submit"]')

    async def fill_and_submit_noemail(self, name, message):
        await self.page.fill('input[name="name"]', name)
        await self.page.fill('textarea[id="textarea_comp-kzzez81j"]', message)
        await self.page.click('button[aria-label="Submit"]')

    async def fill_and_submit_justemail(self, email):
        await self.page.fill('input[name="email"]', email)
        await self.page.click('button[aria-label="Submit"]')

    async def get_error(self):
        await self.page.locator('.error-message').text_content()

    async def get_success(self):
        await self.page.locator('.success-message').text_content()
        