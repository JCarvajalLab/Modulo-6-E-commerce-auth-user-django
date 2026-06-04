# DESARROLLO DE APLICACIONES WEB CON PYTHON DJANGO (V2)

## Tabla de contenidos
- [DESARROLLO DE APLICACIONES WEB CON PYTHON DJANGO (V2)](#desarrollo-de-aplicaciones-web-con-python-django-v2)
    - [Tabla de contenidos](#tabla-de-contenidos)
    - [Instrucciones](#instrucciones)
    - [Construido con](#construido-con)
    - [Instalación y ejecución del proyecto](#instalación-y-ejecución-del-proyecto)
    - [Rutas principales](#rutas-principales)
    - [Usuarios de prueba](#usuarios-de-prueba)
    - [Evidencia](#evidencia)
    - [GitHub Repositorio](#github-repositorio)
    - [Estructura del proyecto](#estructura-del-proyecto)
    - [Autor](#Autor)

## Instrucciones 
Implementar un sistema de autenticación de usuarios en una aplicación web desarrollada con 
Django, incorporando páginas de inicio de sesión y cierre de sesión, así como vistas protegidas que 
permitan diferenciar el acceso a determinadas secciones del e-commerce.

## Construido con

* Python `3.14+`
* pip
* Visual Studio Code
* SQLite3 
* Windows 11

## Instalación y ejecución del proyecto
### Entrar a la carpeta:

```bash
cd ecommerce
```

---

### Crear entorno virtual

```bash
python -m venv venv
```

---

### Activar entorno virtual

```bash
venv\Scripts\activate
```
---

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### Ejecutar servidor

```bash
python manage.py runserver
```
---
### Abrir proyecto
http://127.0.0.1:8000/

---

## Rutas principales

| Ruta        | Descripción          | Requiere login|
| ----------- | -------------------- |---------------|
| /           | Página principal     |      No       |
| /register/  | Registro de usuarios |      No       |
| /login/     | Inicio de sesión     |      No       |
| /dashboard/ | Vista protegida      |      Si       |
| /products / | Vista protegida      |      Si       |

---

## Usuarios de prueba

Los siguientes usuarios están disponibles para probar la aplicación:

| Usuario | Email | Contraseña |Rol|
|---------|-------|------------|---|
| `boss` | `boss@gmail.com` | `123` |`SuperUser`|
| `felipe` | `null`| `pipe1234` |`usuario comun`|
| `jordan` | `null`| `jor12345` |`usuario comun`|
| `jose` | `null`| `pepe12345` |`usuario comun`|
> [!NOTE]
> Al crear un nuevo usuario solo es permitido crear un usuario comun.
> El super usuario fue creado con el comando `createsuperuser` en la consola para temas de prueba

## Evidencia 
### Pagina principal
![alt text](static/images/image1.png)
## Registro de usuarios
![alt text](static/images/image2.png)
> [!NOTE]
> El formulario queda desordenado por que se utilizo
> solo el formulario predeterminado de {{ form.as_p }} en Django
## Inicio de sesion
![alt text](static/images/image3.png)
> [!NOTE]
> El formulario queda desordenado por que se utilizo
> solo el formulario predeterminado de {{ form.as_p }} en Django
## Pagina principal luego de iniciar sesion
![alt text](static/images/image4.png)
## DashBoard
![alt text](static/images/image5.png)
## Productos
![alt text](static/images/image6.png)
## Intento de entrar al `Dashboard` desde la URL sin iniciar sesion(Redirije automaticamente a `/login`)
![alt text](static/images/image7.png)
![alt text](static/images/image8.png)
## GitHub Repositorio

[https://github.com/JCarvajalLab/Modulo-6-E-commerce-auth-user-django](https://github.com/JCarvajalLab/Modulo-6-E-commerce-auth-user-django)

## Estructura del proyecto

```
└── 📁ecommerce
    └── 📁accounts
        └── 📁migrations
            ├── __init__.py
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── 📁ecommerce
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
    └── 📁static
        └── 📁css
            ├── styles.css
        └── 📁images
            ├── image1.png
            ├── image2.png
            ├── image3.png
            ├── image4.png
            ├── image5.png
            ├── image6.png
            ├── image7.png
            ├── image8.png
    └── 📁templates
        └── 📁accounts
            ├── dashboard.html
            ├── login.html
            ├── products.html
            ├── register.html
        └── 📁components
            ├── footer.html
            ├── navbar.html
        ├── base.html
        ├── home.html
    ├── db.sqlite3
    ├── manage.py
    ├── README.md
    └── requirements.txt
```

## Autor

**Actividad Final - Modulo 6 - Desarrollo Portafolio**

**Alumno:** Jordan Carvajal - **Fecha:** 03-06-2026



