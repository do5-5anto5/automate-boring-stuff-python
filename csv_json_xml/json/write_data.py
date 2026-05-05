import json

python_dict = {
    "name": "Alice Doe",
    "age": 30,
    "car": None,
    "programmer": True,
    "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"},
    "phone": [
        {"type": "mobile", "number": "415-555-7890"},
        {"type": "work", "number": "415-555-1234"},
    ],
}

# parse Python string data to json data
# attribute intedent=2 fprmats Json text into separate lines, with 2 spaces indenting each nested dict or list
json_string = json.dumps(python_dict, indent=2)

# printing string
print(json_string)
