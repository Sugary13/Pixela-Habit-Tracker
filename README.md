# 📊 Pixela Habit Tracker
Un proyecto simple que utiliza la API de Pixela para rastrear hábitos diarios como el ciclismo, lectura, meditación, etc. Automatiza la creación de usuarios, gráficos, registros diarios (pixeles) y operaciones CRUD usando requests, variables de entorno con dotenv, y fechas con datetime.

# 🚀 Funcionalidades
- ✅ Crear usuario en Pixela (1ª vez)

- 📈 Crear un gráfico para seguimiento de hábitos

- 🟢 Registrar una entrada diaria (pixel)

- ✏️ Actualizar una entrada existente

- ❌ Eliminar una entrada (pixel)

- 🔒 Uso seguro de claves API con .env

# 📦 Tecnologías utilizadas
- Python 3

- requests

- python-dotenv

- Pixela API

- datetime

- .env para gestión de secretos

# 📁 Estructura del código

```bash
load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = "sugary17"
GRAPH_ID = "graph1"
```

```python
# Las funciones principales están comentadas para que actives según la operación que desees realizar:

# Crear usuario
# requests.post(url=pixela_endpoint, json=user_params)

# Crear gráfico
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Añadir nuevo pixel
# requests.post(url=pixela_creation_endpoint, json=pixel_config, headers=headers)

# Actualizar pixel
# requests.put(url=pixela_put_endpoint, json=pixel_update_config, headers=headers)

# Eliminar pixel
requests.delete(url=pixela_put_endpoint, headers=headers)
```

# 🛠️ Cómo usar
1. Clona el repositorio.

2. Crea un archivo .env con esta estructura:

```
TOKEN=tu_token_de_pixela
```

3. Ejecuta main.py según la acción que desees (crear usuario, registrar entrada, etc).

