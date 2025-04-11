from playwright.sync_api import sync_playwright


def test_add_task():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://todomvc.com/examples/react/dist/#/")
        page.get_by_test_id("text-input").click()
        page.get_by_test_id("text-input").fill("test001")
        page.get_by_test_id("text-input").press("Enter")
        assert page.locator('text-input').inner_text() == "test001"
        browser.close()