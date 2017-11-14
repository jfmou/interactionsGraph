import os
import sys

# Builtins
TOP_LEVEL_DIR = os.path.abspath(os.curdir)
API_ENDPOINT = "0.0.0.0"
API_PORT = 5443
DEBUG = True

# Uploads
UPLOADED_FILES_ALLOW = ['csv']
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/api/static/uploads'
UPLOADED_CSV_DEST = TOP_LEVEL_DIR + '/api/static/csv'

