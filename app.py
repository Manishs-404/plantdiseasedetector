import sqlite3
import uuid
import requests
from flask import Flask, request, render_template, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key-change-in-production"  # MUST BE SET

# ------------------------------------------------------------------
# 1. DB helper
# ------------------------------------------------------------------
def get_disease_info(tag):
    conn = sqlite3.connect("plant_diseases.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT cause, remedy, organic_medicine FROM remedies WHERE full_tag = ?",
        (tag,),
    )
    row = cur.fetchone()
    conn.close()
    return row

# ------------------------------------------------------------------
# 2. Azure credentials 
# ------------------------------------------------------------------
prediction_key = "PLACEHOLDER"
prediction_endpoint = "PLACEHOLDER" 
#upload credentials from the azure custom vision model
# ------------------------------------------------------------------
# 3. Login / Logout / Check Auth
# ------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing fields"}), 400

   
    session["user"] = username
    return jsonify({"success": True, "username": username})

@app.route("/logout")
def logout():
    session.pop("user", None)
    return jsonify({"success": True})

@app.route("/check-auth")
def check_auth():
    user = session.get("user")
    return jsonify({"authenticated": bool(user), "username": user})

# ------------------------------------------------------------------
# 4. Main routes
# ------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image"}), 400
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    try:
        headers = {
            "Prediction-Key": prediction_key,
            "Content-Type": "application/octet-stream",
        }
        resp = requests.post(prediction_endpoint, headers=headers, data=file.read())
        resp.raise_for_status()
        data = resp.json()

        # Get top prediction
        top = data["predictions"][0]
        disease_tag = top["tagName"]
        confidence = top["probability"] * 100  # convert to %

        # THRESHOLD: 85%
        if confidence < 85:
            return jsonify({
                "disease": "Not Recognized",
                "confidence": f"{confidence:.1f}%",
                "message": "Plant disease data not found. The image may be unclear or the plant/disease is not in our database."
            })

        # If confident enough → fetch from DB
        cause = remedy = organic = "No information found."
        info = get_disease_info(disease_tag)
        if info:
            cause, remedy, organic = info

        return jsonify({
            "disease": disease_tag,
            "confidence": f"{confidence:.1f}%",
            "cause": cause,
            "remedy": remedy,
            "organic": organic,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
