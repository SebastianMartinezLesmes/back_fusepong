from fastapi import FastAPI
from routes.endpoints import router as endpoints_router
from config.cors import configure_cors

app = FastAPI()

# Configurar CORS
configure_cors(app)

# Incluir rutas
app.include_router(endpoints_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
