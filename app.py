from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# LangFlow API Configuration
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "32281cfb-4cc4-4c77-b716-cc9848a326cf"
ENDPOINT = "social"
APPLICATION_TOKEN = "AstraCS:gHSEpttgMcQjTSwhRPEZBTMt:1f37fbff64273fb594d54cfe2eb8aa961604c90b8789b78c27b2340d72066336"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message")
    url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "input_value": user_message,
        "output_type": "chat",
        "input_type": "chat"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.ok:
            # Extract bot's reply from the response JSON
            bot_message = response.json().get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "Error: No reply from bot.")
            return jsonify({"bot_message": bot_message})
        else:
            return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
