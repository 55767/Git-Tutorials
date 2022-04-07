import json
data = '{"var1":"kushal", "var2":"rabi"}'
parsed = json.loads(data)
print(parsed['var1'])
print(parsed)
print(type(parsed))

data2= {
    "channel name":"kushal vlogs", "cars":"rolls royace",
    "fridge":('roti', 'hukka'), "files":[1,'k xa']
}

jscomp = json.dumps(data2)
print(jscomp)