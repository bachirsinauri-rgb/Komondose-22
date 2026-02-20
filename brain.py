import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# استدعاء المفتاح من البيئة (نظام الحماية السيادي)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/ask', methods=['GET'])
def ask():
    user_query = request.args.get('q')
    if not user_query:
        return jsonify({"reply": "نظام الرائد ينتظر أمرك..."})
    
    try:
        response = model.generate_content(user_query)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"خطأ تقني: {str(e)}"})

if __name__ == '__main__':
    # المنفذ 8080 للمطابقة التامة مع GitHub
    app.run(host='0.0.0.0', port=8080)
