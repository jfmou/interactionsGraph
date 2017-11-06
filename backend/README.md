# Backend

Backend is a python Flask application

## Requirements

```
* Python (>= 3.4)
* docker (only for dev purposes) 
```

## Installation

### Clone this repository

```
bzhtux@localhost: ~# git clone -b poc-backend-python https://github.com/jfmou/interactionsGraph.git
```
If you already have cloned this repository just point it to poc-backend-python branch: 

```
bzhtux@localhost: ~# git fetch --all
bzhtux@localhost: ~# git checkout poc-backend-python
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

 * [Build](#Build) docker image


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
bzhtux@localhost: ~# docker run -ti --rm -p 5000:5000 ig-backend-dev:0.0.1 bash
```

## Usage

You can call the backend API without any Auth like this curl command:

```
curl -sL -k http://0.0.0.0:5000/api/datas | jq
```

## Development

### Organization

```
bzhtux@localhost: ~# tree -I "__pycache__"
.
├── Makefile
├── README.md
├── __init__.py
├── api
│   ├── __init__.py
│   ├── commons.py
│   ├── models.py
│   └── views
│       ├── __init__.py
│       └── default.py
├── data.csv
├── docker
│   ├── Dockerfile
│   ├── entrypoint.sh
├── instance
│   ├── dev.py
│   ├── prod.py
│   └── test.py
├── requirements.txt
└── run.py
```
* **api** folder: all python files required by API
* **instance** folder: configuration folder, each file for a dedicated env
* **docker** folder: files required to build docker image (makefile copy required python files into docker directory before building the image)
* **api/views** folder: really ??? Yes API views ('/api/blabla')
* **requirements.txt** file: python dependancies

### TODO

* write a bunch of tests
* write some qa/ci enforcements
* validate this poc ;-)