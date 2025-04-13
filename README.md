# 🍽️ Django Recipe App with Spoonacular API

Web application developed with **Django** that allows users to search for recipes using the **Spoonacular API**, save them to their personal profiles, and manage their favorite recipes easily and intuitively. This project was developed as part of the Web Project course.

---

## 🔗 GitHub Repository

[https://github.com/your-repo-here](https://github.com/your-repo-here) <!-- Replace with your real link -->

---

## 🧠 Project Objective

The goal of this project is to develop a functional and personalized web application that allows users to:

- Search for cooking recipes through an external API.
- View detailed information for each recipe (ingredients, instructions, images, etc.).
- Create a user account and save favorite recipes for easy access at any time.

All within a clean, user-friendly and intuitive interface.

---

## 🧩 Implemented Features

- ✅ Django admin panel enabled (`/admin`)
- ✅ User registration and authentication (`/register`, `/login`, `/logout`)
- ✅ Recipe search via Spoonacular API
- ✅ Detailed recipe view (ingredients, instructions, image)
- ✅ Ability to save and manage favorite recipes
- ✅ HTML template system with inheritance (`base.html`)
- ✅ Custom styling with CSS and responsive layout
- ✅ Dockerized project (`Dockerfile`, `docker-compose.yml`)
- ✅ Follows 12-factor app principles

---

## ☝️ Design Considerations

- **External API:** The Spoonacular API was chosen to access a rich and well-structured recipe database.
- **User Experience:** The design focuses on easy and intuitive navigation, with quick access to key functionalities.
- **Code Modularity:** Logic is organized into separate Django apps to improve maintainability and scalability.
- **Security:** Basic validation and access control mechanisms were implemented for user management.
- **Containers:** Docker was used to ensure the project is portable and easy to run on any system.

---

## ▶️ Running the Project

### 1. Install dependencies

```bash
  poetry install
```

### 2. Migrate the database

```bash
  python manage.py makemigrations
  python manage.py migrate
```

### 3. Start the server

```bash
  python manage.py runserver
```

Once the server is running, access the app at:  
[http://localhost:8000](http://localhost:8000)

### 4. Access the admin panel

First, create a superuser:

```bash
  python manage.py createsuperuser
```

Then, log in at:  
[http://localhost:8000/admin](http://localhost:8000/admin)

---

## 👥 Developers

- Ainhoa Ferradas Romero  
- Marc Ferreres Zaragoza  
- Edna Solans Viscasillas  
- Abril Tufet Coll

