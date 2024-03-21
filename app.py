from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app = FastAPI()

#Configurar Cors por si las dudas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Enpoint get para obtener el hola mundo
@app.get("/hola_mundo")
async def get_hola_mundo():
    return "Hola mundo"

# Rutas para servir la documentación de Swagger
@app.get("/docs", include_in_schema=False)
async def get_swagger_html():
    return app.swagger_ui_html

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
    return get_openapi(app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
