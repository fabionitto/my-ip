from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def send_ip():
    data = {
        'ip': request.remote_addr,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(threaded=True)
