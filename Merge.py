import json
import glob;
files=[];
merged = list()

for filename in glob.glob("*.json"):
    files.append(filename);

for filename in files:
    with open(filename, "r") as a_file:
        a_file = json.load(a_file)
        a_file = a_file["Activity"]
        for x in a_file:
            keys = x.keys()
            values = x.values()
            merged.append(list(values))
        


merged = json.dumps(merged, indent=4)
merged = merged[1:]
merged = merged[:-1]
print(merged)
with open('merged.txt', 'w') as table:
    table.write("insert into activity values"+ merged)




