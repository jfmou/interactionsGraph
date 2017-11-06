from api import app
from api.commons import Utils
from flask import jsonify

utils = Utils()


@app.route("/", methods=['GET'])
def index():
    rows = utils.read_csv_file("./data.csv")
    return jsonify({"rows": rows}), 200


@app.route("/api", methods=['GET'])
def index_api():
    rows = utils.read_csv_file("./data.csv")
    return jsonify({"rows": rows}), 200

@app.route("/api/datas", methods=['GET'])
def get_json_data():
    csv_data = utils.read_csv_file("./data.csv")
    nodes = utils.build_nodes_from_csv(csv_data)
    links = utils.build_links_from_csv(csv_data)
    return jsonify({"nodes": nodes, "links": links}), 200
