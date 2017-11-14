import csv
import hashlib
from functools import partial


class Utils():

    def __init__(self):
        self.COLORS = {'OK': '#00ff00',
                  'Moyen': '#ff9900',
                  'Pas d\'interaction': '#999',
                  'NOK': '#ff0000',
                  'DEFAULT': '#fff'
                }

    def read_csv_file(self, csv_file_path):
        csv_data = list()
        with open(csv_file_path) as csv_fd:
            csvdata = csv.DictReader(csv_fd, delimiter=',')
            for row in csvdata:
                csv_data.append(row)
        return csv_data

    def build_nodes_id_from_csv(self, nodes):
        nodes_id = [node['id'] for node in nodes]
        return nodes_id

    def build_nodes_from_csv(self, csv_data):
        #data = self.read_csv_file("./data.csv")
        nodes = list()
        for row in csv_data:
            if row['↓ pense que ses relations avec → sont'] not in nodes:
                nodes.append({"id": row["↓ pense que ses relations avec → sont"], "group": ""})
        return nodes

    def build_links_from_csv(self, csv_data):
        links = list()
        for row in csv_data:
            # print("> %s\n" % row['↓ pense que ses relations avec → sont'])
            source = row['↓ pense que ses relations avec → sont']
            for item in row:
                if row['↓ pense que ses relations avec → sont'] != row[item] and row['↓ pense que ses relations avec → sont'] != item:
                    # print(" - %s : %s" % (item, row[item]))
                    target = item
                    try:
                        value = self.COLORS[row[item]]
                    except:
                        value = self.COLORS['DEFAULT']
                    links.append({"source": source, "target": target, "value": value})
        return links

    def get_uploaded_file_hash(self, upload_path, uploaded_file):
        hash_md5 = hashlib.md5()
        with open("%s/%s" % (upload_path, uploaded_file), "rb") as file_fd:
#            for chunk in iter(lambda: file_fd.read(4096), b""):
#                hash_md5.update(chunk)
            for buf in iter(partial(file_fd.read, 128), b''):
                hash_md5.update(buf)
        return hash_md5.hexdigest()
