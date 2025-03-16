# Transport Management System

The goal of this assignment is to assess your ability to work with a full-stack application using Vue.js with TypeScript on the frontend and Django on the backend. You will be required to create a simple logistics Order Management system that consists of an Order model and a Waypoint model, where multiple waypoints can be attached to a single order

- **Frontend**: Minimalistic UI built with Vue.js, Tailwind CSS
- **Backend**: Built using Django with Django REST Framework (DRF)

## Table of Contents

- [Installation](#installation)
- [Frontend](#frontend-development)
- [Backend](#backend-development)
- [Deployment](#deployment)

## Installation

### Frontend (Vue.js)

1. Navigate to the frontend directory:

    ```bash
    cd app
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

---

### Backend (Django with Django REST Framework)

1. Navigate to the backend directory:

    ```bash
    cd api
    ```

2. Set up a Python virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. Install the required Python dependencies:

    ```bash
    pip install
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

---

## Frontend Development

1. **Start the Vite Development Server**:

    ```bash
    npm run dev
    ```

   This will start the frontend app at `http://localhost:3000`.

2. **API URL Configuration**: 
   By default, the API URL is set to `http://localhost:8000` for local development. To switch development and production environments use `.env` file.

---

## Backend Development

1. **Start the Django Development Server**:

    ```bash
    python manage.py runserver
    ```

   This will start the backend API at `http://localhost:8000`.

2. **API Endpoints**:

   - **GET /api/orders/**: List all transport orders with pagination, filtering, and sorting.
   - **POST /api/orders/**: Create a new transport order.
   - **GET /api/orders/{id}/**: Retrieve details for a specific transport order.

---


## Deployment

//TODO