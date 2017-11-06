from api.commons import Utils
from flask import Flask
import os
import sys

sys.path.append(os.path.abspath(os.curdir))
app = Flask(__name__, instance_relative_config=True)

# Try to get env from SHELL ENV
# Set to 'prod' by default
try:
    env = os.environ['FLASK_ENV']
except Exception as e:
    print("+++ Error loading env: %s" % e)
    print("+++ Setting env to default: production")
    env = "prod"

print("\033[32mENV: %s\033[0m" % env)

# Load the config file regarding env above
if env == "dev":
    app.config.from_pyfile('dev.py')
if env == "test":
    app.config.from_pyfile('test.py')
if env == "prod":
    app.config.from_pyfile('prod.py')

try:
    import api.views
except Exception as e:
    print("init.imports.except: %s" % e)
