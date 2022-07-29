import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'django-simple-cms'
AUTHOR = 'Rafael Ricardo Pinto'
AUTHOR_EMAIL = 'rafaga2469@gmail.com'
URL = 'https://github.com/rafaga2469'

LICENSE = 'MIT'
DESCRIPTION = 'CMS sencillo para admin de django'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'Django>=4.0.6',
    'django-bootstrap5>=21.3',
    'django-ckeditor>=6.4.2',
    'django-colorfield>=0.7.2',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      license=LICENSE,
      packages=find_packages(),
      include_package_data=True)
