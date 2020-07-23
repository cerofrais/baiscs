from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET,POST'])
def index():
    print(request.headers)
    print(request.json)
    print(request.body)

    return jsonify("success"),200

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',  port=1111)

