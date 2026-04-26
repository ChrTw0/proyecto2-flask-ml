# Proyecto 2 — Backend Flask ML + App Flutter MVC

Sistema completo compuesto por un **backend Flask** con un modelo de Machine Learning y una **app móvil en Flutter** que consume el servicio. La app permite ingresar una temperatura en grados Celsius y obtener su equivalente en Fahrenheit usando predicción con regresión lineal.

---

## Preguntas que cubre

- **P4** — Backend Flask con modelo ML + App Flutter que consume el servicio
- **P5** — Patrón de diseño MVC aplicado en Flutter

---

## Estructura del proyecto

```
proyecto2-flask-flutter/
├── flask-backend/          Backend API REST con modelo ML
└── flutter-app/            App móvil con patrón MVC
```

---

## Flask Backend

### Tecnologías
- Python 3.11
- Flask 3.1
- scikit-learn (LinearRegression)
- NumPy
- Gunicorn

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/predict` | Recibe `{"celsius": 100}` y retorna `{"celsius": 100, "fahrenheit": 212.0}` |
| GET | `/health` | Verifica que el servicio esté activo |

### Correr localmente

```bash
cd flask-backend
pip install -r requirements.txt
python app.py
```

### Deploy en Render

1. Crea una cuenta en [render.com](https://render.com) e inicia sesión
2. Click en **New → Web Service**
3. Selecciona **Build and deploy from a Git repository**
4. Conecta tu cuenta de GitHub y selecciona el repositorio `proyecto2-flask-ml`
5. Render detecta el `render.yaml` automáticamente y completa los campos:
   - **Runtime:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click en **Create Web Service**
7. Espera que el build termine (1-2 minutos) — verás `==> Build successful 🎉`
8. Copia la URL pública que aparece en la parte superior, ejemplo:
   `https://proyecto2-flask-ml.onrender.com`
9. Pega esa URL en `flutter-app/lib/view/temperature_view.dart`:
   ```dart
   static const _backendUrl = 'https://proyecto2-flask-ml.onrender.com';
   ```

> **Nota:** En el plan gratuito de Render el servicio se duerme tras 15 minutos de inactividad. La primera petición puede tardar ~30 segundos en responder.

---

## Flutter App

### Tecnologías
- Flutter 3.x + Dart 3
- Paquete `http` para consumir la API
- Patrón MVC implementado manualmente

### Patrón MVC aplicado

```
lib/
├── main.dart                          Punto de entrada
├── model/
│   ├── temperature_model.dart         Entidad de datos (Celsius + Fahrenheit)
│   └── temperature_repository.dart    Interfaz + implementación HTTP (ITemperatureRepository)
├── controller/
│   └── temperature_controller.dart    Lógica de negocio + estado (ChangeNotifier)
└── view/
    └── temperature_view.dart          UI + widgets visuales
```

**Modelo** → representa los datos y la comunicación con la API  
**Vista** → muestra la interfaz y reacciona a cambios del controlador  
**Controlador** → maneja la lógica, valida entradas y notifica a la vista

---

## Cómo correr la app en VS Code

### 1. Instalar la extensión de Flutter

1. Abre **Visual Studio Code**
2. Ve a **Extensiones** (`Ctrl+Shift+X`)
3. Busca `Flutter` (publicada por **Dart Code**)
4. Click en **Instalar** — instala también Dart automáticamente

Documentación oficial: https://docs.flutter.dev/tools/vs-code

### 2. Abrir el proyecto

**Archivo → Abrir carpeta** → selecciona la carpeta `flutter-app/`

### 3. Instalar dependencias

Abre la terminal integrada (`Ctrl+ñ`) y ejecuta:

```bash
flutter pub get
```

### 4. Agregar soporte de plataforma (solo la primera vez)

```bash
flutter create --platforms=windows .
```

### 5. Seleccionar dispositivo

En la barra inferior de VS Code aparece el selector de dispositivo. Elige **Windows** para correr como app de escritorio.

### 6. Correr la app

Presiona **F5** o ejecuta en terminal:

```bash
flutter run -d windows
```
