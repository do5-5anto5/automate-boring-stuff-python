from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=2500)
# use attr headless=False to open phisical browser like selenium does
# slow_mo=3000 add a 3000 ms delay to its operations so that it’s easier to show what is happening
# just to study case - to slowly show what is happening

page = browser.new_page()
page.goto('https://autbor.com/example3.html')

page.locator('#login_user').fill('Real Name')
page.locator('#login_pass').fill('swordfish')
page.locator('input[type=submit]').click()

browser.close()
playwright.stop()