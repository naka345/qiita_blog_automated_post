from flask import Flask, jsonify, request, render_template, redirect ,url_for
from oauthlib.oauth2 import WebApplicationClient
import urllib
import json
from script.qiita_api import QiitaApi
import requests
import os
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hello !!!!!!!!!!!!!!"

@app.route("/redirect", methods=['GET'])
def redirect_qiita_api():
    token = request.args.get('code')
    #items_dict = read_items(code)
    return redirect(url_for("success"),token=token, code=302)

@app.route("/success", methods=['GET'])
def all_passed():
    token = request.args.get("token")
    return f"all passed!! {yoken}"

@app.route("/q_api", methods=['GET'])
def call_qiita_api():
    api = QiitaApi()
    scope = ["read_qiita", "write_qiita"]
    url, state = api.call_authorization_url(scope=QiitaApi.define_scope(scope))

    print(url)
    return redirect(url, code=302)

def check_code_exist(code=None):
    if code is None and os.environ.get("code"):
        code = os.environ.get("code")
    print(f"code: {code}")
    return code

@app.route("/q_api/read_items", methods=['POST'])
def read_items(code=None):
    # could change class member var ....
    code = check_code_exist(code=code)
    api = QiitaApi()
    api.access_tokens(code)
    items = api.get_item()
    pick_up_keys = ["title","url","body","private"]
    items_dict = api.adjust_item(items,pick_up_keys)
    return items_dict

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
