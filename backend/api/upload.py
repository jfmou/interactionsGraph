from api import app
from api.commons import Utils
from flask_uploads import UploadSet, configure_uploads
import os
import time

# Configure the image uploading via Flask-Uploads
data_csv = UploadSet('datacsv', 'csv')
configure_uploads(app, data_csv)
utils = Utils()

class Upload():

    def __init__(self, filename=None):
        self.filename = filename

    def upload_file(self, filename=None):
        if filename is None:
            return False
        self.filename = filename
        try:
            data_csv.save(self.filename)
            return True
        except Exception as e:
            print("Upload.upload_file.except: %s" % e)
            return False

    def file_already_exists(self, filename=None):
        if filename is None:
            return True
        md5 = utils.get_uploaded_file_hash("%s/datacsv" % app.config['UPLOADS_DEFAULT_DEST'], filename)
        if os.path.isfile("%s/%s-hash_%s" % (app.config['UPLOADED_CSV_DEST'],
                                          filename,
                                          md5
                                        )
                        ):
            return True
        else:
            return False

    def remove_file(self, file_path=None, filename=None):
        if file_path is None or filename is None:
            return False
        if os.remove("%s/%s" % (file_path, filename)):
            return True
        else:
            return False

    def move_uploaded_file(self, filename=None):
        if filename is None:
            return False
        md5 = utils.get_uploaded_file_hash("%s/datacsv" % app.config['UPLOADS_DEFAULT_DEST'], filename)
        os.rename("%s/datacsv/%s" % (app.config['UPLOADS_DEFAULT_DEST'], filename),
                  "%s/%s-hash_%s" % (app.config['UPLOADED_CSV_DEST'],
                                filename,
                                md5
                      )
                )
        if os.path.islink("%s/data.csv" % app.config['UPLOADED_CSV_DEST']):
            os.unlink("%s/data.csv" % app.config['UPLOADED_CSV_DEST'])
        os.symlink("%s/%s-hash_%s" % (app.config['UPLOADED_CSV_DEST'],
                                      filename,
                                      md5
                                    ),
                   "%s/data.csv" % app.config['UPLOADED_CSV_DEST'])
        return True
