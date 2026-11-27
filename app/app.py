from flask import Flask, jsonify

app = Flask(__name__)
loans = []

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/loans", methods=["GET"])
def list_loans():
    return jsonify(loans)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
