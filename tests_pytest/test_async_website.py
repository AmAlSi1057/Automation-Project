import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
from pages_models.async_form import form
from pages_models.async_navigation import navigation
from pages_models.async_mobile import mobile


@pytest_asyncio.fixture(scope="session")
async def browser_launch():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            yield page
        finally:
            await page.close()
            await context.close()
            await browser.close()


@pytest.mark.asyncio
async def test_navigation(browser_launch):
    """Test Navigation Links"""
    navigation_page = navigation(browser_launch)
    
    await navigation_page.go_to_home()
    await navigation_page.nav_to_about_us()
    assert await navigation_page.get_title() == "About | Arpeely", "Navigation to About Us failed!"
    
    await navigation_page.go_to_home()
    await navigation_page.nav_to_contact()
    assert await navigation_page.get_title() == "Contact Us | Arpeely", "Navigation to Contact Us failed!"       


@pytest.mark.asyncio
async def test_form_submission(browser_launch):
    """Test Form Validation on Contact Page"""
    form_page = form(browser_launch)
    
    await form_page.goto_contact()
    
    # Test submitting an empty form
    await form_page.empty_submit()
    error_message = await form_page.get_error()
    assert "This field is required" in error_message, "Form validation failed!"
    
    # Test submitting an invalid form without email
    await form_page.fill_and_submit_noemail('John Doe', 'This is a test message.')
    success_message = await form_page.get_success()
    
    #Test submitting an invalid form with only email
    #await form_page.fill_and_submit_justemail('test@test.com')
    #success_message = await form_page.get_success()

    assert "Thank you for your message!" in success_message, "Form submission failed!"


@pytest.mark.asyncio
async def test_responsive_design(browser_launch):
    """Test Mobile Responsiveness"""
    mobile_page = mobile(browser_launch)

    await mobile_page.set_viewport('iPhone 13')
    await mobile_page.mobile_home()
    assert await mobile_page.visible_mobile_menu() is True
