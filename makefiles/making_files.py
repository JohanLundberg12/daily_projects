import json
import pathlib

p = pathlib.Path("settings", "config.json")
d = json.loads(p.read_text())

path_to = pathlib.Path("data", "configuration.json")
# rename p and save it to path_to (the file in settings folder is gone)
p.rename(path_to)

path_to.rename(p)  # rename back to the original name in original folder

text = json.dumps(d)
pathlib.Path("data", "config-1.json").write_text(text)
