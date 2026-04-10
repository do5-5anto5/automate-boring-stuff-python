from playwright.sync_api import sync_playwright

def click_elements():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=3000)
        # use attr headless=False to open phisical browser like selenium does
        # slow_mo=3000 add a 3000 ms delay to its operations so that it’s easier to show what is happening
        # just to study case - to slowly show what is happening
        
        page = browser.new_page()
        page.goto('https://autbor.com/example3.html?')

        page.click('input[type=checkbox]') # checks the checkbox
        page.click('input[type=checkbox]') # unchecks the checkbox
        page.click('a') # click the link
        page.go_back()
        
        checkbox_elem = page.get_by_role('checkbox') # calls locator method

        checkbox_elem.check() # checks the checkbox
        checkbox_elem.uncheck() # unchecks the checkbox
        checkbox_elem.set_checked(True) # checks the checkbox
        checkbox_elem.set_checked(False) # unchecks the checkbox

        page.get_by_text('is a link').click() # uses locator than click

        browser.close()

click_elements()