from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8100"],  # Origen permitido
        allow_credentials=True,
        allow_methods=["*"],  # Métodos permitidos
        allow_headers=["*"],  # Encabezados permitidos
    )
