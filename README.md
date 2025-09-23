# API de Embeddings con Flask y OpenRouter

Esta es una API RESTful creada con Flask que utiliza **OpenRouter** para interactuar con las Inteligencias Artificiales.

## Tabla de contenido

1. [Requisitos previos](#requisitos-previos)
2. [Configuración del proyecto](#configuración-del-proyecto)
3. [Ejecución del proyecto](#ejecución-del-proyecto)
4. [Uso de la API](#uso-de-la-api)
5. [Despliegue](#despliegue)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**: Descárgalo desde [python.org](https://www.python.org/downloads/).
- **Git**: (Opcional) Para clonar el repositorio.
- **Una clave API de OpenRouter**: Regístrate en [OpenRouter](https://openrouter.ai/) para obtener tu clave API.

---

## Configuración del proyecto

### 1. Clonar el repositorio

Si estás usando Git, clona este repositorio:

```bash
git clone https://github.com/tu-usuario/embedding-api.git
cd embedding-api
```

### 2. Crear un entorno virtual
Crea un entorno virtual para aislar las dependencias del proyecto:

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

En macOS/Linux:
```
bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instalar dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:
```
bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto y agrega tu clave API de OpenRouter:
```
plaintext
OPENROUTER_API_KEY=tu_clave_api_de_openrouter
```
Este archivo será cargado automáticamente por la biblioteca python-dotenv.

### Ejecución del proyecto
Activa el entorno virtual (si no está activo):

En Windows:
```
bash
venv\Scripts\activate
```
En macOS/Linux:
```
bash
source venv/bin/activate
```

### Ejecuta la aplicación Flask:

```
bash
python app.py
```
La API estará disponible en http://127.0.0.1:5000