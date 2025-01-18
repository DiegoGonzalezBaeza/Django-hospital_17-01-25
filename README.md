# Django-hospital_17-01-25
Proyecto educativo

# Hospital Management System

Este proyecto es un sistema de gestión hospitalaria desarrollado con **Django** para el backend y **Django** también para el frontend. 

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
DJANGO-HOSPITAL/
├── backend/           # Contiene el proyecto backend
│   ├── GestionHospital/
│   ├── api_hospital/
│   ├── db.sqlite3
│   └── manage.py
├── frontend/          # Contiene el proyecto frontend
│   ├── hospital/
│   ├── db.sqlite3
│   └── manage.py
├── venv/              # Entorno virtual de Python
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación del proyecto
```

## Requisitos Previos

Asegúrate de tener instalados los siguientes elementos antes de continuar:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

---

## Instrucciones de Instalación y Ejecución

### Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd DJANGO-HOSPITAL
```

---

### Configurar el Entorno Virtual

1. Crear el entorno virtual:

   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Instalar las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

---

### Configurar y Ejecutar el Backend

1. Navegar a la carpeta del backend:

   ```bash
   cd backend
   ```

2. Aplicar las migraciones:

   ```bash
   python manage.py migrate
   ```

3. Ejecutar el servidor de desarrollo del backend:

   ```bash
   python manage.py runserver
   ```

   El backend estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Configurar y Ejecutar el Frontend

1. En una nueva terminal (mantén el backend ejecutándose), navega a la carpeta del frontend:

   ```bash
   cd frontend
   ```

2. Aplicar las migraciones:

   ```bash
   python manage.py migrate
   ```

3. Ejecutar el servidor de desarrollo del frontend:

   ```bash
   python manage.py runserver 8080
   ```

   El frontend estará disponible en: [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

### Notas Adicionales

- Asegúrate de tener ambos servidores (backend y frontend) corriendo simultáneamente.
- Configura correctamente los **CORS** en el backend para permitir las solicitudes desde el frontend.

---

## Licencia

Este proyecto está bajo la licencia