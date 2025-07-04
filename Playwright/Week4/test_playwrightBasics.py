from playwright.async_api import Page

def test_playwrightBasics(playwright):
    # playwright is the global fixture, that contains browser invoking and setup things
    browser = playwright.chromium.launch(headless=False)
    # chromium.launch just a method to call the browser
    context = browser.new_context()
    # new_context is the method that use to open a fresh incognito page and stores the cache and data
    page = context.new_page()
    page.goto("https://playwright.com/")

def test_playwrightShortcut(page:Page):
    # Page is a class that contains so many methods, so using that we call Page class from the playwright.async_api package
    # Using page fixture straight forward, we can skip first 3 lines of code what we wrote in the above function
    # But using page, it only runs in the headless mode and always configured and open chromium engine and 1 single context
    page.goto("https://playwright.com/")

#For running from Terminal "pytest test_playwrightBasics.py::test_playwrightShortcut --headed"
