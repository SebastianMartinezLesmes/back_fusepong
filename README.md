## Pre-requisitos
Antes de comenzar con la creación del proyecto en FastAPI, asegúrate de cumplir con los siguientes requisitos:

1. **Tener una Base de Datos (MongoDB Compass)**
  1. Descargar MongoDB Compass en su [Pagina Oficial](https://www.mongodb.com/try/download/compass).
  2. Instalar MongoDB Compass.
  3. Iniciar MongoDB Compass.
  4. Inicia la base de datos en el puerto: mongodb://localhost:27017.

2. **Instalar Python**
- Descarga e instala Python (versión 3.8 o superior) desde su sitio web oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Durante la instalación, asegúrate de marcar la casilla "Add Python to PATH" para facilitar el uso de Python desde la terminal.
Verifica que Python se instaló correctamente ejecutando el siguiente comando en tu terminal o consola:
```prompt
python --version
```
O
```prompt
python -V
```

3. **Instalar pip** (Gestor de paquetes de Python)
- En la mayoría de las instalaciones de Python, pip ya viene preinstalado. Verifica su instalación ejecutando:
```prompt
pip --version
```
O
```prompt
pip -V
```

Si no está instalado, puedes instalarlo siguiendo las instrucciones oficiales: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

4. **Instalar Git**
- Instala Git para gestionar tu proyecto con control de versiones. Descárgalo desde: [https://git-scm.com/](https://git-scm.com/)
- Verifica su instalación ejecutando:
```prompt
git --version
```
O
```prompt
git -V
```

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

- En el servidor local: Para acceder a la aplicación en tu servidor local, abre [http://localhost:8000](http://localhost:8000) en tu navegador

- Documentación interactiva de la API está disponible en [http://localhost:8000/docs](http://localhost:8000/docs)

6. **Estructura**

back_fusepong/
├── .venv/                        # Entorno virtual
├── config/                       # Configuraciones del proyecto
│   └── cors.py                     # Configuración para el manejo de CORS
├── model/                        # Modelos del proyecto
│   ├── data/                       # Datos estáticos o ejemplos
│   │   ├── fusepong.corporations.json  # Datos sobre corporaciones
│   │   ├── fusepong.proyects.json      # Datos sobre proyectos
│   │   ├── fusepong.tickets.json       # Datos sobre tickets
│   │   └── fusepong.users.json         # Datos sobre usuarios
│   └── model.py                    # Archivo que define modelos o estructuras de datos
├── routes/                       # Rutas o endpoints de la API
│   └── endpoints.py                # Archivo con las rutas de la aplicación
├── .gitignore                    # Archivos y carpetas a ignorar por Git
├── main.py                       # Punto de entrada principal de la aplicación
├── README.md                     # Documentación del proyecto

## Notas
1. **Verificar el estado de la Base de Datos:**
Antes de iniciar el backend, asegúrate de que la base de datos esté funcionando correctamente para evitar errores de conexión.
2. **Repositorio del Frontend:**
El repositorio del frontend del proyecto está disponible en el siguiente enlace: [Front](https://github.com/SebastianMartinezLesmes/front_fusepong)
