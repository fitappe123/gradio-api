from flask import Flask, request, jsonify
from gradio_client import Client, handle_file
import os

app = Flask(__name__)
client = Client("AlaaElsayed/yolospace")  # عدّلي لو الSpace مختلف

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "image_url" not in data:
        return jsonify({"error": "Missing image_url"}), 400

    result = client.predict(
        image=handle_file(data["image_url"]), 
        api_name="/predict"
    )

    return jsonify({
        "detected_image": result[0],
        "nutrition_info": result[1]
    })

@app.route("/")
def home():
    return "✅ API is running"

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
