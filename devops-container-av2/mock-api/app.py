from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint raiz
@app.route('/')
def home():
    return jsonify({"message": "Mock API is running!"})

# Endpoint de dados simulados
@app.route('/data')
def get_data():
    return jsonify({
        "id": 1,
        "name": "Mock Item",
        "description": "This is a simulated response.",
        "price": 19.99,
        "in_stock": True
    })

# Outro endpoint de exemplo
@app.route('/status')
def status():
    return jsonify({"status": "All systems operational", "uptime": "48 hours"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)