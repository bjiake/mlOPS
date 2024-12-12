from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    data = request.get_json()
    if data is None:
        data = request.args
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)