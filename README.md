# About Project 

[Complete guide | Run This Project on your computer](https://github.com/danialafjeh/Run-My-Projects-Locally)

# Calorie Tracker

A full-stack calorie tracking web application built with **Django** using the **MVT architecture**, with a complete frontend and backend, PostgreSQL database, and Dockerized environment.

> **Important:** This project is intended for educational and demonstration purposes only. It is **not a medical or clinical tool** and must not be used for real medical, nutritional, or health-related decisions.

---

## 📌 Overview

**Calorie Tracker** is a Django-based web application that allows users to create personalized calorie reports based on their physical information and the foods they consume.

The main focus of this project was the implementation of a complete **Django backend**, including authentication, authorization, data validation, database relationships, calorie calculation logic, user dashboards, and finally **Dockerizing the entire application**.

The frontend was also fully implemented and customized using **HTML, CSS, and JavaScript**.

---

## Features

### User Authentication & Authorization

The application provides a complete authentication and authorization system:

* User registration
* User login and logout
* Authentication and session management
* Permission and access control
* Separation between regular users and administrators
* Different access levels for different types of users
* Protection of unauthorized pages and actions
* Display of the current user's access level in their profile dashboard

Administrators and regular users have separate access levels, and the application checks whether the requested action is permitted before allowing access.

---

### User Profile & Dashboard

Every registered user has their own profile dashboard.

Users can:

* View their personal account information
* View their body information
* Edit their account information
* Edit their physical/body information
* View their previous calorie reports
* Open individual reports and see their complete details
* View their current user/access level

The dashboard provides users with a centralized place to manage their information and review their previous usage of the calorie tracking tool.

---

## Calorie Tracker Logic

The main functionality of the application is the calorie tracking tool.

Before calculating a report, the application uses information provided by the user, including:

* Age
* Gender
* Height
* Weight
* Physical activity level

The user then adds the foods they have consumed **one by one**.

Each food entry contains information required for the calorie calculation, including its quantity and unit.

### Food Units

The application supports different measurement types:

* `gram`
* `ml`
* `piece`

The calculation logic depends on the selected unit.

For foods measured in **grams or milliliters**, calories are calculated based on the food's calorie value per 100 units:

```text
Calories = (Quantity / 100) × Calories per 100g/100ml
```

For foods measured by **piece**:

```text
Calories = Quantity × Calories per piece
```

The application processes all added foods and calculates their total calorie value.

---

## Calorie Calculation

The application estimates the user's daily calorie requirement using established calculation formulas.

### 1. BMR — Mifflin–St Jeor Equation

The user's **Basal Metabolic Rate (BMR)** is estimated using the **Mifflin–St Jeor equation**.

BMR represents the estimated amount of energy the body requires at rest.

### 2. TDEE — Total Daily Energy Expenditure

The application then calculates the user's estimated daily energy expenditure:

```text
TDEE = BMR × Physical Activity Level
```

The selected physical activity level determines the activity multiplier used in the calculation.

The resulting TDEE represents an estimate of the calories the user may require throughout a normal day based on their physical activity level.

### 3. Calorie Balance

The application compares the total calories consumed through the entered foods with the estimated TDEE:

```text
Calorie Balance = Total Food Calories − TDEE
```

This result is then used to determine the user's reported calorie condition.

---

## Body / Calorie Condition

After calculating the report, the application categorizes the result into one of three conditions:

### 1. LOW

The user's consumed calories are **less than 90% of their estimated TDEE**.

```text
Total Calories < 90% of TDEE
```

This indicates that the recorded calorie intake is relatively low compared with the estimated daily energy expenditure.

### 2. NORMAL

The user's consumed calories are between **90% and 110% of their estimated TDEE**.

```text
90% ≤ Total Calories ≤ 110% of TDEE
```

This indicates that the recorded calorie intake is within the application's defined normal range relative to estimated TDEE.

### 3. HIGH

The user's consumed calories are **more than 110% of their estimated TDEE**.

```text
Total Calories > 110% of TDEE
```

This indicates that the recorded calorie intake is relatively high compared with the estimated daily energy expenditure.

> These categories are application-defined informational classifications and should not be interpreted as medical or nutritional diagnoses.

---

## Interactive Food Entry

The calorie tracking interface is designed to provide immediate feedback while entering foods.

When a user adds foods one by one:

1. The food data is validated.
2. The food is added to the current report.
3. The newly added food immediately appears in the table beside the input section.
4. The user can continue adding additional foods.
5. The user can use **Reset** to clear the currently added foods.
6. The user can use **Calculate** to process the complete list and generate the calorie report.

This allows users to review their entered foods before performing the final calculation.

---

## Data Validation

Validation is applied throughout the calorie tracking process to prevent invalid or meaningless data from being used in calculations.

The application validates the information entered for each food, including:

* Quantity
* Measurement unit
* Calorie values
* Numeric values
* Food information required for calculation

The application also prevents inappropriate numeric input, such as invalid decimal formats or meaningless values, from being accepted.

All food data used by the calorie calculation logic is validated before being processed.

This helps prevent invalid input from reaching the calculation layer and producing unreliable results.

---

## Django Forms

The project makes extensive use of **Django Forms** for handling and validating user input.

Forms are used for different parts of the application, including:

* User-related information
* Body information
* Food information
* Calorie tracking data
* Editing existing information

Validation is handled through Django's form system as well as additional application-level validation where necessary.

---

## Django Messages Framework

The application uses Django's built-in **Messages Framework** to provide notifications and feedback to users.

Messages are used to inform users about events such as:

* Successful operations
* Invalid input
* Authentication-related events
* Updates
* Errors
* Other important actions performed throughout the application

This provides immediate feedback without requiring separate notification systems.

---

## Database

The application uses **PostgreSQL** as its database.

The database stores information related to:

* Users
* User profiles/body information
* Foods
* Calorie reports
* Food entries
* User-specific report history

Relationships between the application's models are handled through Django's ORM.

---

## Dockerized Environment

The project has been fully **Dockerized**.

Docker is used to containerize the application and its database environment.

The project includes:

* Django application container
* PostgreSQL database container
* Docker Compose configuration
* Database health checking
* Environment-based configuration
* Persistent database storage

The Docker setup allows the project to be started without manually configuring the entire Django/PostgreSQL environment on the host machine.

---

## 🎨 Frontend

The frontend was developed using:

* JavaScript
* HTML
* CSS
* Bootstrap

The project uses a modern responsive frontend design.

The original frontend templates were based on resources from **ThemeWagon**:

https://themewagon.com/

The templates were then:

* Customized
* Modified
* Integrated with Django
* Connected to the application's backend
* Extended with new pages
* Adapted to the application's functionality

---

## Technologies Used

### Backend

* Python
* Django 6.0.7
* Django MVT
* Django ORM
* Django Forms
* Django Authentication
* Django Messages Framework

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* PostgreSQL

### Docker

* Docker Desktop
* Docker Hub
* Dockerfile
* Docker Compose
* Docker Networking
* Images
* Containers
* Volume

---

## 🎯 Project Goals

The primary goal of this project was to build and understand a complete Django application from the backend side and then prepare it for being a containerized project using Docker.

Particular focus was placed on:

* Django backend architecture
* MVT architecture
* Django ORM
* Database relationships
* Forms and validation
* Authentication
* Authorization
* Access control
* User dashboards
* Business logic
* Calorie calculation
* Data validation
* PostgreSQL integration
* Dockerizing & Containerized application

The frontend was implemented as a complete interface for the backend functionality, while the main learning and development focus of the project was the **backend logic and Dockerization process**.
