from playwright.sync_api import sync_playwright

def find_elements():
    
    """
    Finds all <p> elements on the webpage https://autbor.com/example3.html, prints the text of the first
    element, and prints the HTML source of the first element.

    This function demonstrates how to use Playwright to synchronous (pause while loading) launch a
    Chrome browser, navigate to a webpage, and retrieve information from the page.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=3000) 
        # use attr headless=False to open phisical browser like selenium does
        # slow_mo=3000 add a 3000 ms delay to its operations so that it’s easier to show what is happening
        # just to study case - to slowly show what is happening
        
        page = browser.new_page()
        page.goto('https://autbor.com/example3.html')

        elems = page.locator('p')
        print(elems.nth(0).inner_text())
        print(elems.nth(0).inner_html())

find_elements()