# init file for my site's python package
# The create_app function is used to create the site
# using the included pages.
#
# pages.py specifies page routes
# wsgi.py is used by mod_wsgi-express to actually host the site

import subprocess

subprocess.run(['sh', './update-containers.sh'])

