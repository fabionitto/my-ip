from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    if not request.headers.getlist("X-Forwarded-For"):
        ip = request.remote_addr
    else:
        ip = request.headers.getlist("X-Forwarded-For")[0]
    data = {
        'ip': ip,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
