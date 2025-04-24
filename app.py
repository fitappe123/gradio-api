from flask import Flask, request, jsonify
from gradio_client import Client, handle_file

app = Flask(__name__)
client = Client("AlaaElsayed/yolospace")  # عدّلي إذا كان Space مختلف

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "image_url" not in data:
        return jsonify({"error": "Missing image_url"}), 400

    # نرسل للصورة للـ Space
    result = client.predict(
        image=handle_file(data["image_url"]),
        api_name="/predict"
    )
    # نعيد جزئي الاستجابة
    return jsonify({
        "detected_image": result[0],
        "nutrition_info": result[1]
    })

@app.route("/")
def home():
    return "✅ API is running"

if __name__ == "__main__":
    app.run(debug=True)
