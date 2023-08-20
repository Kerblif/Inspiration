import json
from tome import Tome

raw_tomes = json.loads(open("./data/jsons/tomes.json").read())["elements"]
parsed_tomes = dict()

for i in raw_tomes:
    tmp = Tome(i)
    parsed_tomes[tmp.id] = tmp

print(parsed_tomes["t.naeniansketches"])