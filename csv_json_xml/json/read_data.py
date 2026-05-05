import json, pprint

json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer": true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"}, {"type": "work", "number": "415-555-1234"}]}'

# parse json string to Python string value with json load string method
python_data = json.loads(json_string)
print(type(python_data))  # this is a dict

# print value as formatted text
pprint.pprint(python_data)
