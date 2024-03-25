from flask import Flask, jsonify
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost") 

app = Flask(__name__)

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

def set_key(key, value):
    r.set(key, value)

def get_key(key):
    return r.get(key)

@app.route("/set/<key>/<value>", methods=["GET"])
def set_key_value(key, value):
    set_key(key, value)
    return jsonify({"msg": "Key set"})

@app.route("/get/<key>", methods=["GET"])
def get_key_value(key):
    value = get_key(key)
    if value is None:
        return jsonify({"msg": "Key not found"})
    return jsonify({"msg": value.decode("utf-8")})

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"msg": "Eu estou saudavel"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
