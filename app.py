from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>CI/CD Pipeline Project</title>
        <style>
            body {{
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }}
            .box {{
                background: rgba(0,0,0,0.3);
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
            }}
            h1 {{
                font-size: 40px;
            }}
            p {{
                font-size: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 CI/CD Pipeline Web App</h1>
            <p><b>Status:</b> Running Successfully</p>
            <p><b>Version:</b> 4.0</p>
            <p><b>Hostname:</b> {hostname}</p>
            <p><b>Time:</b> {time}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

