import os
from pathlib import Path
from this import d
from flask import Flask, request
from git import Repo
import git as gitMod


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Simple Server for webhooks ==> Kali"


home_directory = str(Path.home())


def send_email_to_contributors_mock():
    """
    Sends email to contributors of the repo
    """
    pass


@app.route("/payload/", methods=["POST"])
def handle_hooks():
    clone_url = request.json["repository"]["clone_url"]
    repo_name = request.json["repository"]["name"]

    project_directory = os.path.join(home_directory, repo_name)

    if not os.path.exists(project_directory):
        Repo.clone_from(clone_url, project_directory)

    git = gitMod.cmd.Git(project_directory)
    git.pull()

    send_email_to_contributors_mock()

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(port="8000")
