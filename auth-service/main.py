from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/register', methods=['POST'])
def register():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)