from flask import Flask, jsonify, request
import json
from script.qiita_api import QiitaApi
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    api = QiitaApi()
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

if __name__ == "__main__":
    app.run()
