from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def render(template_path, context):
    template = env.get_template(template_path)
    return template.render(**context)