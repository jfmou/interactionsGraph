# Backend

Backend is a python Flask application

## Requirements

```
* Python (>= 3.4)
* docker (only for dev purposes)
* ig-backend-dev:0.0.2
```

## Installation

### Clone this repository

```
bzhtux@localhost: ~# git clone -b poc-backend-python https://github.com/jfmou/interactionsGraph.git
```
If you already have cloned this repository just point it to poc-backend-python branch: 

```
bzhtux@localhost: ~# git fetch --all
bzhtux@localhost: ~# git checkout ${current_branch}
```

### Native install

I suggest you to use a virtualenv to run this python app. To create a virtualenv with python3 just run:

```
bzhtux@localhost: ~# mkdir -p ~/.venvs
bzhtux@localhost: ~# python3 -m venv ~/.venvs/interGraph
```

To use this virtualenv, run:

```
bzhtux@localhost: ~# source ~/.venvs/interGraph/bin/activate
(interGraph) bzhtux@localhost: ~# 
```

Now go back to your git workspace and install python dependancies:

```
(interGraph) bzhtux@localhost: ~# cd Workdir/Python3x/interactionsGraph
(interGraph) bzhtux@localhost: interactionsGraph# pip install -r backend/requirements.txt
```
That's all for native installation step!

### Docker install

Docker installation is very simple:

 * [Build](#build) docker image


## Build

To build docker image, you can use Makefile provided with this command:

```
bzhtux@localhost: ~# make build-docker
```

## Run

### Native

```
bzhtux@localhost: ~# make run
```

### Docker

Use `-ti` for interactive console:

```
bzhtux@localhost: ~# docker run -ti --rm -p 5000:5000 ig-backend-dev:0.0.2 bash
```

## Usage

You can call the backend API without any Auth.

### GET json data collection from csv

```
bzhtux@localhost: ~# curl -sL -k http://0.0.0.0:5000/api/datas | jq
```

### POST new csv data collection

```
bzhtux@localhost: ~# curl -i -X POST -F csv_file=@/tmp/data.csv http://0.0.0.0:5000/api/uploads
```

## Development

### Organization

```
bzhtux@localhost: ~# tree -d -I "__pycache__"
.
├── api
│   ├── static
│   │   ├── csv
│   │   └── uploads
│   │       └── datacsv
│   └── views
├── docker
└── instance
```
* **api** folder: all python files required by API
* **instance** folder: configuration folder, each file for a dedicated env
* **docker** folder: files required to build docker image (makefile copy required python files into docker directory before building the image)
* **api/views** folder: really ??? Yes API views ('/api/blabla')
* **api/static** folder: static files
* **api/static/uploads** folder: upload dir
* **api/static/csv** folder: csv files dir

### TODO

* write a bunch of tests
* write some qa/ci enforcements
* validate this poc ;-)