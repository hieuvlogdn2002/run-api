from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/apifl", methods=["GET"])
def apifl():
    fl1 = request.args.get("fl1", "")

    if not fl1:
        return jsonify({"status": "error", "message": "Thiếu fl1"}), 400

    return jsonify({
        "status": "success",
        "data": fl1
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
