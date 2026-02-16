from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")

def home():

    return jsonify({

        "Project": "CI/CD Pipeline for Web Application",

        "Status": "Running Successfully",

        "Version": "2.0",

        "Hostname": socket.gethostname(),

        "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    })


@app.route("/health")

def health():

    return "Application Healthy", 200


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

