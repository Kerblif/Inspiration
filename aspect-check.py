import json
from aspect import Aspect

raw_aspects = json.loads(open("./data/jsons/_aspects.json").read())["elements"]
parsed_aspects = dict()

for i in raw_aspects:
    tmp = Aspect(i)
    parsed_aspects[tmp.id] = tmp

print(parsed_aspects["reading.winter.intro"])