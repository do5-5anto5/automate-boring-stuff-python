# For small projects, XML can be written directly with open() and write().
# The xml.etree module is available, but requires creating a root element
# and building the structure using SubElement().

import xml.etree.ElementTree as ET

person = ET.Element('person') # Create the root XML element.
name = ET.SubElement(person, 'name') # Create <name> and put it under <person>.
name.text = 'Alice Doe' # Set the text between <name> and </name>.
age = ET.SubElement(person, 'age')
age.text = '30' # XML content is always a string.
programmer = ET.SubElement(person, 'programmer')
programmer.text = 'true'
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')
car.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
address = ET.SubElement(person, 'address')
street = ET.SubElement(address, 'street')
street.text = '100 Larkin St.'

# Remaining <address> and <phone> elements are omitted for brevity.
# Use ET.tostring(root).decode() to convert the XML tree into a string.
decoded_string = ET.tostring(person, encoding='utf-8').decode('utf-8')
print(decoded_string)