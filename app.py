from flask import Flask
from routes.embeddings import embeddings_bp
from routes.health import health_bp
from routes.open_router import open_router_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(health_bp, url_prefix="/health")
app.register_blueprint(embeddings_bp, url_prefix="/embed")
app.register_blueprint(open_router_bp, url_prefix="/open-router" )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)