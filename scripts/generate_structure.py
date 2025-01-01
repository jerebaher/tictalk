import os

project_name = "backend"
folders = [
    "app/models",
    "app/routers",
    "app/services",
    "app/schemas",
    "app/tasks"
]

files = {
    "app/__init__.py": "",
    "app/main.py": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'Hello': 'World'}",
    "app/config.py": "# Configuración de variables de entorno",
    "app/db.py": "# Configuración de la DB",
    "Dockerfile": "FROM python:3.10-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ['uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000']",
    "requirements.txt": "fastapi\nuvicorn\ncelery\nredis\nsqlalchemy\nstatsig",
    ".env": "DATABASE_URL=postgresql://user:password@localhost/db",
    "README.md": "# Backend API"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Estructura del proyecto generada correctamente.")