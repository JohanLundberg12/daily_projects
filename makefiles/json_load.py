import json

# will fail on windows machine (\ are used instead of /)
with open("./settings/config.json") as f:
    d = json.loads(f.read())
print("One way of loading the jsoon file: ", d, "\n")


import os

# absolute path of a relative path is relative to the operating system (windows, mac, linux)
p = os.path.abspath(os.path.join("settings", "config.json"))
print("Absolute path: ", p, "\n")

print(os.path.exists(p))  # True

import pathlib

print(pathlib.Path("settings", "config.json").exists())  # True

p = pathlib.Path("settings", "config.json")
print("Read the file as text: ", p.read_text(), "\n")  # read the file as text
print(
    "Parse the valid json string and convert it to python dictionary format: ",
    json.loads(p.read_text()),
    "\n",
)

print("The parts of the path: ", p.parts, "\n")
print("Is this a directory? ", p.is_dir(), "\n")
print("Is this a file? ", p.is_file(), "\n")
print(
    "Get the absolute path of the relative path and compare to the original path: ",
    p.resolve().samefile(p),
    "\n",
)

print("Type of file: ", p.suffix, "\n")
