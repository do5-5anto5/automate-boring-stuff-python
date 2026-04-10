from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=2500)
# use attr headless=False to open phisical browser like selenium does
# slow_mo=3000 add a 3000 ms delay to its operations so that it’s easier to show what is happening
# just to study case - to slowly show what is happening

page = browser.new_page()
page.goto('https://reddit.com')

page.locator('html').press('End') # scrolls to bottom
page.locator('html').press('Home') # scrolls to top

browser.close()
playwright.stop()