from jinja2 import Environment, select_autoescape, FileSystemLoader
from config import BASE_DIR

env = Environment(
    loader=FileSystemLoader(BASE_DIR / 'templates/'),
    autoescape=select_autoescape(['html', 'xml'])
)