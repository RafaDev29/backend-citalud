# 🩺 Django REST API - Sistema de Gestión Médica

![Logo del Proyecto](https://i.imgur.com/AfFp7pu.png)

Este proyecto es una API RESTful construida con Django y Django REST Framework. Permite la gestión de pacientes, citas médicas, atenciones, medicamentos y servicios médicos adicionales.

---

## 📦 Requisitos

- Python 3.10 o superior
- pip
- Virtualenv (opcional pero recomendado)
- PostgreSQL o SQLite3
- Git

---

## 🚀 Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto

python -m venv env
source env/bin/activate   # En Windows: env\Scripts\activate

pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate

python manage.py runserver
