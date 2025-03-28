import pytest
import json
from playwright.async_api import async_playwright

@pytest.mark.asyncio
@pytest.mark.parametrize("scenario, mock_response", [
    ("normal", [{"id":1, "advertiser":"Nike", "bid":5.00, "ad_text":"Buy a new sneakers!"},
                {"id":2, "advertiser": "Adidas", "bid":4.20, "ad_text":"50% off today"}]),
    ("no_ads", []),
    ("slow", [{"id":3, "advertiser":"Puma", "bid":6.00, "ad_text":"New running shoes!"}]),
    ("error", "server_error")]) #Running the function with multiple sets of data (input, expected)
async def test_ad_bidding_scenarios(scenario,mock_response):
    async with async_playwright() as p:
        browser= await p.chromium.launch(headless=True)
        context= await browser.new_context()
        page= await context.new_page()

        async def mock_ads(route): #a function to mock API responses
            if scenario == "error":
                await route.fulfill(status=500, body="internal server error")
            elif scenario == "slow":
                await route.fulfill(status=200, context_type="application/json", body=json.dump(mock_response), delay=5000)
            elif scenario == "normal":
                await route.fulfill(status=200, context_type="application/json", body=json.dump(mock_response))
        
        await page.route("https://adserver.com/api/bids", mock_ads) #Intercepts the requests and return mocked responses
        await page.goto("https://adplatform.com") #loading the page that makes API calls to fetch the ads
        #testing UI based on scenario
        if scenario == "no_ads":
            no_ads_message = await page.inner_text("#no-ads-message")
            assert no_ads_message == "No ads available!"
        elif scenario == "error":
            error_message = await page.inner_text("#error-message")
            assert error_message == "Failed to load ads"
        elif scenario == "slow":
            loading_spinner = await page.is_visible("#leading-spinner")
            assert loading_spinner is True
        elif scenario == "normal":
            ad_text = await page.inner_text("#ad-text")
            assert ad_text == "Buy a new sneakers!"
    
        await browser.close()





