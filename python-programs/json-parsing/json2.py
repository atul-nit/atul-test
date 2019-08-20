import json

data = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}
#
# print(type(data))
# print(data)
# jstr = json.dumps(data)
# print(type(jstr))
# print(jstr)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)