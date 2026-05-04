import os
from flask import Flask, send_from_directory, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 載入 .env 檔案中的環境變數
load_dotenv()

app = Flask(__name__, static_folder='static')

# 初始化 Gemini 客戶端
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def read_index():
    # 回傳靜態資料夾中的 index.html
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    message = data.get("message", "")
    
    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview", # 使用指定的 Gemini 模型
            contents=message,
            config=types.GenerateContentConfig(
                system_instruction="You are Gemini, a helpful AI assistant."
            )
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
