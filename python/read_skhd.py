# this file will read the browser shortcuts from my skhdrc
# it creates a list of shortcut objects
from pathlib import Path
import re

# get path to skhdrc file, where the shortcuts are stored
# expand ~ to be user home directory
p = Path("~/.config/skhd/skhdrc").expanduser()

f = open(p, "r")
skhdrc = f.read()

shortcuts = []


class Shortcut:
    def __init__(self, prefix, letter, url):
        self.letter = letter
        self.url = url
        self.prefix = prefix


# use regex to find the shortcut and url in the skhd file
# pattern to find shortcut in skhdrc file
pattern = re.compile(r"cmd[\s\+]*ctrl[\s\+]*alt.*")
matches = pattern.finditer(skhdrc)
for match in matches:
    match_text = match[0]
    prefix = match_text[0:19]
    letter = match_text[19]
    url = match_text[29:-1]
    shortcuts.append(Shortcut(prefix, letter, url))
