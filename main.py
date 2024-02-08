import json
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from html2text import html2text
from weasyprint import HTML, CSS


with open("data.json") as _:
    json_data = json.load(_)
    
env = Environment(loader=FileSystemLoader("."))

template = env.get_template("template.html")
html_content = template.render(items=json_data)

pdf_bytes = HTML(string=html_content).write_pdf(stylesheets=[CSS(filename="style.css")])
with open("output.pdf", "wb") as _:
    _.write(pdf_bytes)