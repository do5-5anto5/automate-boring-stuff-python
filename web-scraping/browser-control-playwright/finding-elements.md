# Playwright’s Locators for Finding Elements

**Locator** | **Locator object returned**
---------- | ----------
page.get_by_role(role, | name=label) Elements by their role and optionally their label
page.get_by_text(text) | Elements that contain text as part of their
inner text
page.get_by_label(label) | Elements with matching <label> text as label
page.get_by_placeholder(text) | <input> and <textarea> elements with matching placeholder attribute values as the text
provided
page.get_by_alt_text(text) | <img> elements with matching alt attribute values as the text provided
page.locator(selector) | Elements with a matching CSS or XPath selector

# Locator Methods

Method | Description
---------- | ----------
get_attribute(name) | Returns the value for the element’s name attribute, such as 'https://nostarch.com' for the href attribute in an <a="https://nostarch.com"> element
count() | Returns an integer of the number of matching elements in this Locator object
nth(index) | Returns a Locator object of the matching element given by the index. For example, nth(3) returns the fourth matching element since index 0 is the first matching element.
first | The Locator object of the first matching element. This is the same as nth(0).
last | The Locator object of the last matching element. If there are, say, five match elements, this is the same as nth(4).
all() | Returns a list of Locator objects for each individual matching element
inner_text() | Returns the text within the element, such as 'hello' in <b>hello</b> 
inner_html() | Returns the HTML source within the element, such as '<b>hello</b>' in <b>hello</b>
click() | Simulates a click on the element, which is useful for link, checkbox, and button elements
is_visible() | Returns True if the element is visible; otherwise, returns False
is_enabled() | For input elements, returns True if the element is enabled; otherwise, returns False
is_checked() | For checkbox or radio button elements, returns True if the element is selected; otherwise, returns False
bounding_box() | Returns a dictionary with keys 'x' and 'y' for the position of the element’s top-left corner in the page, along with keys width' and 'height' for the element’s size