from playwright.sync_api import sync_playwright

def goto_autbor():
    """
    Opens a Firefox browser (headless), navigates to https://autbor.com/example3.html,
    prints the page title, and then closes the browser.

    This function demonstrates how to use Playwright to synchronous (pause while loading) launch a
    Firefox browser, navigate to a webpage, and retrieve information from
    the page.
    """
    with sync_playwright() as playwrite:
        browser = playwrite.firefox.launch()
        page = browser.new_page()

        page.goto('https://autbor.com/example3.html')
        print(page.title())

        browser.close()

goto_autbor()
