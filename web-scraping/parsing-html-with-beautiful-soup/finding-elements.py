import requests, bs4

res = requests.get("https://autbor.com/example3.html")
res.raise_for_status()

# creating a BeautifulSoup object from a request response
# example_soup = bs4.BeautifulSoup(res.text, "html.parser")

with open(
    "web-scraping\\parsing-html-with-beautiful-soup\\example3.html"
) as example_file:
    example_soup = bs4.BeautifulSoup(example_file, "html.parser")


# The select() method returns a ResultSet of Tags
# example of return:
# [<span id="author">Al Sweigart</span>]

# CSS example selectors

    # s_id = example_soup.select("#author")  # match the elemant with a given id attribute

    # s_div = example_soup.select("div")  # match all elements named <div>

    # s_div_whitin_span = example_soup.select(
    #     "div span"
    # )     # All elements named <span> that are within an element named <div>

    # s_div_directly_span = example_soup.select(
    #     "div > span"
    # )     # All elements named <span> that are directly within an element named <div>, with no other element in between

    # s_input_name = example_soup.select(
    #     "input[name]"
    # )     # All elements named <input> that have a name attribute with any value

    # s_input_button = example_soup.select(
    #     'input[type="submit"]'
    # )     # All elements named <input> that have an attribute named type with the value button

# Pass tag value to the str() function to show the HTML tags it represents

elem_author = example_soup.select("#author")  # match the element with a given id
print(f"Author: {elem_author[0].getText}")
author_elem_id = elem_author[0].attrs  # find element attributes
print(author_elem_id)

# Showing the difference between retrieving the text of an element and displaying the element's tag as a string.
p_elems = example_soup.select("p")

first_prgh_tag = str(p_elems[0])
first_prgh_text = p_elems[0].getText()
scnd_prgh_tag = str(p_elems[1])
scnd_prgh_text = p_elems[1].getText()
third_prgh_tag = str(p_elems[2])
third_prgh_text = p_elems[2].getText()

print(
    f"""
Tag: {first_prgh_tag}
Text: {first_prgh_text}
Tag: {scnd_prgh_tag}
Text: {scnd_prgh_text}
Tag: {third_prgh_tag}
Text: {third_prgh_text}"""
)

# search specific text in an element with get() method. it returns None if nothing matches

print(p_elems[1].get("some_nonxistent_phrase") == None)

print(f'\n\n {p_elems}')