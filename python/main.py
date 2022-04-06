import read_skhd
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

myLoader = FileSystemLoader(["../templates", "/default/templates"])

env = Environment(loader=myLoader, autoescape=select_autoescape())

template = env.get_template("index.html")

os.chdir("..")
with open("index.html", "w") as fileObj:
    fileObj.write(template.render(shortcuts=read_skhd.shortcuts))
