import pytest
from playwright.sync_api import sync_playwright
from pages_models.form import form
from pages_models.navigation import navigation

@pytest.fixture(scope="session")
def browser_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_navigation(browser_launch):
    # Test if the About Us page loads
    nav_page = navigation(browser_launch)

    nav_page.go_to_home()
    nav_page.nav_to_about_us()
    assert nav_page.get_title() == "About | Arpeely", "Navigation to About Us failed!"
    
    # Test if the Contact page loads
    nav_page.go_to_home()
    nav_page.nav_to_contact()
    assert nav_page.get_title() == "Contact Us | Arpeely", "Navigation to Contact Us failed!" 


def test_form_submission(browser_launch):
    form_page = form(browser_launch)

    # Test submitting an empty form
    form_page.goto_contact()
    form_page.empty_submit()
    error_message = form_page.get_error()
    assert "This field is required" in error_message, "Form validation failed!"
    
    # Test submitting a valid form 
    form_page.fill_and_submit('John','Hi this is John!', 'John@email.com')
    success_message = form_page.get_success()
    assert "Thank you for your message!" in success_message, "Form submission failed!"

    # Test submitting an invalid form, name and message only 
    form_page.fill_and_submit_noemail('John','Hi this is John!')
    error_message = form_page.get_error()
    assert "This field is required" in error_message, "Form validation failed!"

    # Test submitting an invalid form, email only 
    form_page.fill_and_submit_justemail('John@email.com')
    error_message = form_page.get_error()
    assert "This field is required" in error_message, "Form validation failed!"


def test_page_load_speed(browser_launch):
    browser_launch.goto("https://www.arpeely.com/")
    load_time = browser_launch.evaluate('''() => {
        return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart;
    }''')
    assert load_time < 2000, f"Page load time is too long: {load_time}ms"   

@pytest.mark.skip
def test_https_security(browser_launch):
    browser_launch.goto("https://www.arpeely.com/")
    assert browser_launch.url.startswith("https://"), "The website is not using HTTPS"
        


