from pathlib import Path

from flask import Flask, request
from git import Repo


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Simple Server for webhooks ==> Kali"


home_directory = str(Path.home())


@app.route("/payload/", methods=["POST"])
def handle_hooks():
    clone_url = request.json["repository"]["clone_url"]
    Repo.clone_from(clone_url, home_directory)

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(port="8000")
