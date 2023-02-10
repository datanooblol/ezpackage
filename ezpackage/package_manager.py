import os
from importlib import resources

# DATA_MODULE = '.ezpackage.templates'

class EzPackage:
    """
    """
    def __init__(self,
                 template_package_name:str,
                 template_version:str,
                 template_author:str,
                 template_author_email:str,
                 template_description:str,
                 template_keywords:list,
                ):
        self.setup_dict = {}
        self.setup_dict['template_package_name'] = template_package_name
        self.setup_dict['template_version'] = template_version
        self.setup_dict['template_author'] = template_author
        self.setup_dict['template_author_email'] = template_author_email
        self.setup_dict['template_description'] = template_description
        self.setup_dict['template_keywords'] = template_keywords
        
    def _setup_template(self):
        print(os.getcwd())
        with open('./ezpackage/templates/setup_template.txt', 'r') as f:
            template_str = f.read()
            
#         for k, v in setup_dict().items():
#             template_str = template_str.replace(k, v)
            
#         with open('./ezpackage/template/setup.py', 'w') as f:
#             f.write(template_str)
            
    def run(self):
        self._setup_template()

def setup_template():
    # path = os.path.join(os.getcwd(), 'ezpackage', 'ezpackage', 'templates', 'setup_template.txt')
    template_str = resources.files('ezpackage.ezpackage').joinpath('setup_template.txt').open("r").read()
    # path = os.path.join('.', 'templates','setup_template.txt')
    # with open(path, 'r') as f:
    #     template_str = f.read()