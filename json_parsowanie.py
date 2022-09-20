import json

with open('test.json') as f:
    data = json.load(f)

slownik = dict(data)
# print(slownik.keys())

print(json.dumps(slownik, indent=4, sort_keys=True))

# with open('test2.json', 'w') as json_file:
#     json.dump(slownik, json_file)

# print(type(data))
# print(data)
