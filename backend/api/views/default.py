from api import app
from api.commons import Utils
from api.upload import Upload
from flask import jsonify, request

utils = Utils()
upload = Upload()


@app.route("/", methods=['GET'])
def index():
    rows = utils.read_csv_file("%s/data.csv" % app.config['UPLOADED_CSV_DEST'])
    return jsonify({"rows": rows}), 200


@app.route("/api", methods=['GET'])
def index_api():
    rows = utils.read_csv_file("%s/data.csv" % app.config['UPLOADED_CSV_DEST'])
    return jsonify({"rows": rows}), 200

@app.route("/api/datas", methods=['GET'])
def get_json_data():
    csv_data = utils.read_csv_file("%s/data.csv" % app.config['UPLOADED_CSV_DEST'])
    nodes = utils.build_nodes_from_csv(csv_data)
    links = utils.build_links_from_csv(csv_data)
    return jsonify({"nodes": nodes, "links": links}), 200

@app.route("/api/uploads", methods=['POST'])
def upload_data_file():
    try:
        filename = request.files['csv_file']
    except Exception as e:
        print("upload_data_file.except: %s" % e)
        return jsonify({"status": "error", "description": "Uploaded file not found"}), 404
    if upload.upload_file(filename):
        if upload.file_already_exists(filename.filename):
            upload.remove_file("%s/datacsv" % app.config['UPLOADS_DEFAULT_DEST'], filename.filename)
            return jsonify({"status": "conflict", "description": "File already exists with same md5"}), 409
        try:
            upload.move_uploaded_file(filename.filename)
        except Exception as e:
            print("upload_data_file.except: %s" % e)
            return jsonify({"status": "error", "description": "Uploaded file not found"}), 404
        return jsonify({"status": "uploaded"}), 202
    else:
        return jsonify({"status": "error", "description": "Error uploading file %s" % filename}), 500
