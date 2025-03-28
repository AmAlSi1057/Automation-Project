from playwright.async_api import Page

class navigation:
    def __init__(self, page:Page):
        self.page = page

    async def go_to_home(self):
        await self.page.goto("https://www.arpeely.com/")

    async def nav_to_about_us(self):
        await self.page.click('#comp-kk2odyr61label')
        await self.page.wait_for_selector('h1')

    async def nav_to_contact(self):
        await self.page.click('#comp-kk2odyr65label')
        await self.page.wait_for_selector('h1')
    
    async def get_title(self):
        return await self.page.title()
