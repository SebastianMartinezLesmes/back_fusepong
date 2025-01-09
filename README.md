## Creación de Proyecto

1. **Crear un entorno virtual**

```prompt
python -m venv <nombre_del_entorno>
```

2. **Activar el entorno virtual**

En Windows:
```bash
nombre_del_entorno\Scripts\activate
```

En Linux/Mac:
```bash
source nombre_del_entorno/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

Instalar dependencias: Usa pip dentro del entorno virtual:
```
pip install fastapi 
pip install uvicorn
pip install pymongo
```

Ejecutar tu aplicación FastAPI: Supongamos que el archivo se llama main.py. Usa:
```
set PYTHONDONTWRITEBYTECODE=1 && uvicorn main:app --reload
```