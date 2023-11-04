import json


def create_json(value):
    return json.dumps({"number": value})


create_json(2)


from pathlib import Path

for folder in range(10):
    for filename in range(5):
        p = Path("data" f"f-{folder}", f"file-{filename}.json")

        if not p.parent.exists():
            p.parent.mkdir()
        p.write_text(create_json(folder * filename))
        print(p)

# get all different folders and files with .json
print(list(Path().glob("data/*/*.json")))

print([_ for _ in Path().glob("*/*-4.json")])
