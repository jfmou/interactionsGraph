from api import app


if __name__ == "__main__":
    app.run(ssl_context="adhoc", host=app.config['API_ENDPOINT'], port=app.config['API_PORT'], debug=app.config['DEBUG'])
