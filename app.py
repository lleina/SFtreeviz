from flask import *
from whitenoise import WhiteNoise  # handles static files very fast

app = Flask(__name__)
# app.wsgi_app = WhiteNoise(app.wsgi_app, root, prefix, index_file, autorefresh) #adding linkage to another library
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root="static/",
    prefix="static/",
    index_file="index.htm",
    autorefresh=True,
)


@app.route("/", methods=["GET"])
def hello():
    return make_response("Hi! append /static/ to the URL to see the visualization")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
