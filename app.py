from flask import Flask, request, jsonify
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Groq API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/sentiment"  # Replace with actual Groq API endpoint

app = Flask(__name__)

def analyze_sentiment_groq(reviews):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    positive, negative, neutral = 0, 0, 0
    total_reviews = len(reviews)
    
    for review in reviews:
        payload = {
            "text": review
        }
        
        try:
            response = requests.post(GROQ_API_URL, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes
            sentiment_data = response.json()
            
            # Assuming Groq API returns sentiment scores in the following format
            # {
            #     "positive": 0.8,
            #     "negative": 0.1,
            #     "neutral": 0.1
            # }
            positive += sentiment_data.get('positive', 0)
            negative += sentiment_data.get('negative', 0)
            neutral += sentiment_data.get('neutral', 0)
        
        except requests.exceptions.RequestException as e:
            print(f"Error processing review: {review}\nError: {e}")
            # You can choose to handle errors differently, e.g., skip or halt
            continue
    
    # Calculate average scores
    if total_reviews > 0:
        return {
            "positive": round(positive / total_reviews, 2),
            "negative": round(negative / total_reviews, 2),
            "neutral": round(neutral / total_reviews, 2)
        }
    else:
        return {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename.endswith('.csv'):
        reviews = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        reviews = pd.read_excel(file)
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV or XLSX file."}), 400

    if 'Review' not in reviews.columns:
        return jsonify({"error": "Missing 'Review' column in the file."}), 400

    # Extract review texts
    review_texts = reviews['Review'].dropna().tolist()

    # Analyze sentiment using Groq API
    results = analyze_sentiment_groq(review_texts)

    return jsonify(results), 200

if __name__ == "__main__":
    app.run(debug=True)
