import os
from importlib import resources

def setup_template():
    # path = os.path.join(os.getcwd(), 'ezpackage', 'ezpackage', 'templates', 'setup_template.txt')
    template_str = resources.files('ezpackage.templates').joinpath('setup_template.txt').open("r").read()
    # path = os.path.join('setup_template.txt')
    # with open(path, 'r') as f:
    #     template_str = f.read()
    return template_str