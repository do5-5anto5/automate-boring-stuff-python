import xml.etree.ElementTree as ET

xml_string = """<person><name>Alice Doe</name><age>30</age>
<programmer>true</programmer><car xsi:nil="true" xmlns:xsi=
"http://www.w3.org/2001/XMLSchema-instance"/><address><street>
100 Larkin St.</street><city>San Francisco</city><zip>94102</zip>
</address><phone><phoneEntry><type>mobile</type><number>415-555-
7890</number></phoneEntry><phoneEntry><type>work</type><number>
415-555-1234</number></phoneEntry></phone></person>"""

# access xml generated
root = ET.fromstring(xml_string)
print(root)

# parse xml data from a file
tree = ET.parse("gen_files/my_data.xml")
root = tree.getroot()
# accessing and printing tags from tree

print(f"""{root.tag}
{list(root)}

{root[0].tag}: {root[0].text}
{root[3].tag}: {root[3].text}
{root[4].tag}:
{root[4][0].tag}: {root[4][0].text}


""")

# iterating element tags, icluding chidren
for elem in root.iter():
    print(elem.tag, "--", elem.text)

# we can pass a string to the iter() method to filter XML elements
for elem in root.iter('number'):
    print(elem.tag, "--", elem.text)


# using third party xmltodict module (you can get it at https://pypi.org/project/xmltodict/)
# this module converts XML text to Python dictionary
import xmltodict

python_data = xmltodict.parse(xml_string)
print('\n', python_data)

# However, the parse is not exact.

# notice that in the output the element 'programer' with the string value 'true' and not a boolean. 
# also 'car': {'@xsi:nil': 'true', '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

# One reason the XML standard has fallen to the wayside compared to formats like JSON
