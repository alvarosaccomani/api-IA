from flask import Blueprint, request, jsonify
from sentence_transformers import SentenceTransformer

# Crear el blueprint
embeddings_bp = Blueprint("embeddings", __name__)

# Cargar el modelo una sola vez
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@embeddings_bp.route("/", methods=["POST"])
def generate_embeddings():
    try:
        data = request.get_json()
        texts = data.get("texts", [])

        if not texts or not isinstance(texts, list):
            return jsonify({"error": "Debes enviar una lista de textos en el campo 'texts'"}), 400

        embeddings = model.encode(texts, convert_to_numpy=True).tolist()

        return jsonify({
            "texts": texts,
            "embeddings": embeddings
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500