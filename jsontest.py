import json

data = {
    'a': 'tourists', 
    'b': 'departures', 
    'c': 'customers', 
    'd': 'passengers', 
    'correct': 'd', 
    'Id': 115255,
    'Stem': 'All _________ must complete a visa form upon arrival at Singapore airport.'
}

json_str = json.dumps(data)
print(json_str)

print(data.Stem)