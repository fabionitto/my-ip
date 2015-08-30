from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    data = {
        'ip': request.remote_addr
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
