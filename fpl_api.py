from flask import Flask, jsonify
import requests, os

app = Flask(__name__)

# حط Team ID بتاعك من موقع FPL
TEAM_ID = 3416238 

@app.route("/team")
def get_team():
    url = f"https://fantasy.premierleague.com/api/entry/{TEAM_ID}/event/1/picks/"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    # هنا الفرق: نستخدم PORT من الـ Environment Variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
