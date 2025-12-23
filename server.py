from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return {"server": "alive"}

@app.route('/main')
def main():
    return {"msg": "hello"}

@app.route('/api', methods=["GET"])
def api_get():
    return {"status": "db not ready"}


@app.route('/api', methods=["POST"])
def api_post():
    return {"status": "logged"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)