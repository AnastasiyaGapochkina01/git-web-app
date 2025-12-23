from flask import Flask
app = Flask(__name__)

# FIX some bug
@app.route('/health')
def health():
    return {"server": "alive"}

@app.route('/main')
def main():
    return {"msg": "hello"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)