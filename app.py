from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'app': 'Second Brain SaaS Tunisie', 'version': '0.1.0'})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json or {}
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    # TODO: save to database or send notification
    return jsonify({'success': True, 'message': 'Message recu, merci ' + name + '!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
