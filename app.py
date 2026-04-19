from flask import Flask, render_template
from src.api.routes import chat_bp
from src.config.logging_config import logging
import os

app = Flask(__name__)
app.register_blueprint(chat_bp)

@app.route("/")
def index():
    return render_template('chat.html')

if __name__ == '__main__':
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8080))
    logging.info("Starting Medical Chatbot app")
    app.run(host=host, port=port, debug=debug)
