from playwright.async_api import Page, async_playwright

class mobile:
    def __init__(self, page: Page):
        self.page = page

    async def set_viewport(self, device):
        async with async_playwright() as p:
            device_profile = p.devices[device]
            await self.page.set_viewport_size({
                "width": device_profile["viewport"]["width"],
                "height": device_profile["viewport"]["height"]
            })
            await self.page.evaluate(f"navigator.__defineGetter__('userAgent', function(){{return '{device_profile['user_agent']}';}});")
    
        
    async def visible_mobile_menu(self):
        menu = await self.page.locator('button[aria-label="Open menu"]')
        return await menu.is_visible()
    
    async def mobile_home(self):
        await self.page.goto("https://www.arpeely.com/")