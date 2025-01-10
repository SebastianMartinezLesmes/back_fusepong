## Creación de Proyecto

### 1. Crear un Entorno Virtual

Para crear un entorno virtual, ejecuta el siguiente comando:

```prompt
python -m venv .venv
```

2. **Activar el entorno virtual**

En Windows:
```prompt
.venv\Scripts\activate
```

En Linux/Mac:
```bash
source nombre_del_entorno/bin/activate
```

3. **Instalar dependencias**

```prompt
pip install -r requirements.txt
```

Instalar dependencias: Usa pip dentro del entorno virtual:
```
pip install fastapi 
pip install uvicorn
pip install pymongo
```
4. **Ejecutar tu aplicación FastAPI (Sin Cache)**
```
set PYTHONDONTWRITEBYTECODE=1 && uvicorn main:app --reload
```

5. **Acceso a la Aplicación**

- En el servidor local:
Para acceder a la aplicación en tu servidor local, abre [http://localhost:8000](http://localhost:8000) en tu navegador

- Documentación interactiva de la API está disponible en [http://localhost:8000/docs](http://localhost:8000/docs)

6. **Estructura**

project/
│
├── main.py            # Archivo principal, inicia la aplicación
├── routes/
│   ├── __init__.py    # Indica que es un paquete Python
│   └── endpoints.py   # Contiene las rutas/endpoints
├── config/
│   ├── __init__.py    # Indica que es un paquete Python
│   └── cors.py        # Configuración del middleware de CORS
└── model/
    ├── __init__.py    # Indica que es un paquete Python
    └── model.py       # Modelos de Pydantic
