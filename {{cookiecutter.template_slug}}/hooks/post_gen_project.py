import os
from glob import glob

license_id = '{%raw%}{{ cookiecutter.license_id }}{%endraw%}'

if license_id != 'None':
    os.rename('LICENSE.{%raw%}{{ cookiecutter.license_id }}{%endraw%}', 'LICENSE')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)
