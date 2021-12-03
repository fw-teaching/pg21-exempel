import json


dudes = [
    { "name": "Göran", "age": 42, "likes": "Python" },
    { "name": "Linus", "age": 51, "likes": "C" },
    { "name": "Betty", "age": 100, "likes": "Breakpoints" }  
]

print(dudes[1]["name"])

dudes_j = json.dumps(dudes, indent=4)

with open('dudes.json', 'w') as f:  # w = write
    f.write(dudes_j)

with open('dudes.json') as file_handle:
    json_dudes = file_handle.read()



dudes_back_to_python = json.loads(json_dudes)
print(dudes_back_to_python[0]["name"])



#print(json_contents)
#print(dudes_j)

