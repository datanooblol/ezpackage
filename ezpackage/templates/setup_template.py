import os

def setup_template():
    # path = os.path.join(os.getcwd(), 'ezpackage', 'ezpackage', 'templates', 'setup_template.txt')
    path = os.path.join('.','setup_template.txt')
    with open(path, 'r') as f:
        template_str = f.read()