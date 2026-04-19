from flask import Blueprint, request, jsonify
from src.services.chatbot_service import get_chain, get_response

chat_bp = Blueprint('chat', __name__)
chain = get_chain()

@chat_bp.route('/chat', methods=['POST'])
def chat():
    question = request.json.get('question')
    if not question:
        return jsonify({"answer": "", "status": "error", "message": "question is required"}), 400
    answer = get_response(question, chain)
    return jsonify({"answer": answer, "status": "success"})

@chat_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})
