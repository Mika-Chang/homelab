# init file for my site's python package
# The create_app function is used to create the site
# using the included pages.
#
# pages.py specifies page routes
# wsgi.py is used by mod_wsgi-express to actually host the site

from flask import Flask, request
import logging
import logging.config
import os
import subprocess
import yaml
from yaml.loader import SafeLoader

## Logging Setup ############################################################
logger = logging.getLogger('webhook-manager')
if not os.path.exists('./logs'):
    os.mkdir('logs')


if os.path.exists('./logging_conf.yml'):
    with open('./logging_conf.yml', 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
        logging.config.dictConfig(yaml_data[0])
elif os.path.exists('./webhook_manager/logging_conf.yml'):
    with open('./webhook_manager/logging_conf.yml', 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
        logging.config.dictConfig(yaml_data[0])
else:
    print('Warning: No config file detected for webhook manager logging')

## Define App ###############################################################
app = Flask(__name__)

@app.route('/webhooks')
def webhooks_root():
    print(request.method)
    return 'hooks'

@app.route('/webhooks/github', methods = ['POST', 'GET'])
def github():
    logger.info('github webhook received')
    subprocess.run(['sh', './update-containers.sh'])
    return 'github'

@app.route('/webhooks/test', methods = ['POST', 'GET'])
def test():
    logger.info('test')
    return 'received'
