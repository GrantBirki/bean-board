import boto3 as boto3
from flask import Flask, render_template, jsonify, request, make_response, redirect
import requests
from os import environ
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from TextImage import TextImage

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"webm", "png", "jpg", "jpeg", "gif", "mp4", "mkv", "m4v"}

SESSION = boto3.Session(
    aws_access_key_id=os.environ['S3_KEY'],
    aws_secret_access_key=os.environ['S3_SECRET'],
    region_name='us-east-2')

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # limit to 16MB


@app.route("/health-check")
def health_check():
    return "ok"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def s3_upload(filepath, filename):
    s3 = SESSION.resource('s3')
    BUCKET = "test-bean-board-bucket"
    s3.Bucket(BUCKET).upload_file(filepath, filename)
    os.remove(filepath)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has a text part
        if 'text' in request.form:
            ti = TextImage(request.form['text'], request.form['color'], app.config["UPLOAD_FOLDER"])
            filepath, filename = ti.text_to_image()
            s3_upload(filepath, filename)
            return render_template("success.html")
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            filepath = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            s3_upload(filepath, filename)

            return render_template("success.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
