import json
import csv


# set COLORS
COLORS = {'OK': '#00ff00',
          'Moyen': '#ff9900',
          'Pas d\'interaction': '#999',
          'NOK': '#ff0000',
          'DEFAULT': '#fff'
        }

# Open and read json file
data = list()
with open("./data.csv") as csv_fd:
    # csv_data = csv.reader(csv_fd, delimiter=',')
    csv_data = csv.DictReader(csv_fd, delimiter=',')
    for row in csv_data:
        data.append(row)

# Build nodes
nodes = list()
for row in data:
    # print(" + %s\n" % row['↓ pense que ses relations avec → sont'])
    if row['↓ pense que ses relations avec → sont'] not in nodes:
        nodes.append({"id": row["↓ pense que ses relations avec → sont"], "group": ""})
nodes_id = [node['id'] for node in nodes]
# Build links
links = list()
for row in data:
    # print("> %s\n" % row['↓ pense que ses relations avec → sont'])
    source = row['↓ pense que ses relations avec → sont']
    for item in row:
        if row['↓ pense que ses relations avec → sont'] != row[item] and row['↓ pense que ses relations avec → sont'] != item:
            # print(" - %s : %s" % (item, row[item]))
            target = item
            try:
                value = COLORS[row[item]]
            except:
                value = COLORS['DEFAULT']
            links.append({"source": source, "target": target, "value": value})

# Display result
print(json.dumps({"nodes": nodes, "links": links}))
