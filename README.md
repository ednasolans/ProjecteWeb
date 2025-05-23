# 🍽️ Django Recipe App with Spoonacular API

Web application developed with **Django** that allows users to search for recipes using the **Spoonacular API**, save them to their personal profiles, and manage their favorite recipes easily and intuitively. This project was developed as part of the Web Project course.

---

## 🔗 GitHub Repository

https://github.com/ednasolans/ProjecteWeb

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
- ✅ RDFa markup addded on recipe_detail.html 

---

## ☝️ Design Considerations

- **External API:** The Spoonacular API was chosen to access a rich and well-structured recipe database.
- **User Experience:** The design focuses on easy and intuitive navigation, with quick access to key functionalities.
- **Security:** Basic validation and access control mechanisms were implemented for user management.
- **Containers:** Docker was used to ensure the project is portable and easy to run on any system.

---

## ▶️ Running the Project with Docker

### 1. Build the Docker image

```bash
  docker-compose build
```

### 2. Migrate the database

```bash
  docker-compose run web python manage.py migrate
```

### 3. Start the app

```bash
  docker-compose up
```

Once the server is running, access the app at:  
[http://localhost:8000](http://localhost:8000)

### 4. Access the admin panel

First, create a superuser:

```bash
  docker-compose run web python manage.py createsuperuser
```

Then, log in at:  
[http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🧪 Tests

This project includes a set of behavior-driven tests using **Behave**, executed through **Selenium** and **Splinter**. This tests run through **Google Chrome**. You may also need **ChromeDriver** installed and available in your system PATH.

- For running the tests:
```bash
  python run_behave_tests.py
```

### If you want to run the tests on the Docker container:

- For entering the docker console:
```bash
  docker exec -it <container-id> bash
```

Note: to see the container id you can use

```bash
  docker ps
```

- For running the tests:
```bash
  python run_behave_tests.py
```

This script: 

- Cleans the test database.
- Creates a test user (user1 / testpass123).
- Launches Behave to simulate usage of the app in a browser.

Covered scenarios: 

- Creating a new recipe.
- Editing an existing recipe.
- Deleting a saved recipe.
- Verifying that changes are correctly reflected in the interface.

## 👥 Developers

- Ainhoa Ferradas Romero  
- Marc Ferreres Zaragoza  
- Edna Solans Viscasillas  
- Abril Tufet Coll

