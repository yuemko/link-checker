from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

history = []  # Başarılı ve başarısız girişleri saklamak için

# Denenecek popüler dizinler (Brute-force için)
COMMON_DIRS = [
    "admin", "login", "dashboard", "backup", "test", ".git", ".env",
    "config", "database", "private", "secret"
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check_url():
    data = request.json
    base_url = data.get("url")

    if not base_url:
        return jsonify({"error": "URL belirtilmedi!"}), 400

    results = []
    
    for path in COMMON_DIRS:
        url = f"{base_url.rstrip('/')}/{path}"
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            result = {"url": url, "status": f"Başarılı ({status})" if status == 200 else f"Hata ({status})"}
        except requests.exceptions.RequestException:
            result = {"url": url, "status": "Bağlantı Hatası"}

        results.append(result)

    history.extend(results)
    return jsonify(results)

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
