from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear el blueprint
open_router_bp = Blueprint("open_router", __name__)

# URL base de OpenRouter
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Clave API de OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Encabezados comunes para todas las solicitudes
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

@open_router_bp.route("/list-models", methods=["GET"])
def list_models():
    """
    Endpoint para listar todos los modelos disponibles en OpenRouter.
    """
    try:
        # Construir la URL completa
        url = f"{OPENROUTER_BASE_URL}/models"

        # Realizar la solicitud GET a OpenRouter
        response = requests.get(url, headers=HEADERS)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": response.text}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@open_router_bp.route("/chat-model", methods=["POST"])
def chat_model():
    """
    Endpoint para chatear contra OpenRouter.
    """
    try:
        req = request.get_json()
        model = req.get("model")
        message = req.get("message")
        print(model)
        print(message)

        # Creo el cliente
        client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL)

        #Creo el chat
        chat = client.chat.completions.create(
            #model = "deepseek/deepseek-chat-v3.1:free",
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        # Convierte el objeto chat a un diccionario
        chat_dict = chat.model_dump() if hasattr(chat, "model_dump") else chat.__dict__

        # Devuelve el diccionario como JSON
        return jsonify(chat_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 500