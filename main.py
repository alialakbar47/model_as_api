from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline("zero-shot-classification",
                  model="facebook/bart-large-mnli")


@app.route('/sentiment', methods=['POST'])
def sentiment():
    """Endpoint to analyze sentiment of provided text."""
    data = request.json
    
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    
    candidate_labels = ["positive", "negative", "neutral"]
    
    # Classify text
    model = get_model()
    if(model is not None):
         results = model(text, candidate_labels,multi_label=True)
         response = {label: round(score, 4) for label, score in zip(results["labels"], results["scores"])}
    else:
       response ={"error": "An error has occured"}
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)