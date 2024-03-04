from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Load your trained model
model_path = "path_to_your_saved_model"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    input_text = request.json.get("input_text")
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400
    
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return jsonify({"response": output_text})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
