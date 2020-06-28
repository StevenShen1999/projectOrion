from flask import Flask, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__)

# The only two routes we need, no backend/frontend intergration needed
@app.route("/serve", methods=['GET'])
def serve_file():
    # TODO: Change this to serve the actual file when hosting this on AWS
    return send_from_directory("resume.pdf")

@app.route("/send", methods=['POST'])
def send_email():
    # TODO: Work with flask's mail component
    pass

CORS(app)

if __name__ == "__main__":
    app.run()