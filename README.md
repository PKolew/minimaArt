# Minima Art Project

## Overview
Minima Art is a Django-powered web application designed to serve as an online art shop. The application provides a comprehensive platform for managing art products, galleries, and reviews, while offering role-based access for admins, staff, and regular users.

---

## Features

### General
- Fully responsive custom-designed frontend.
- Role-based access control for admins and staff.
- Secure authentication system with login, register, and logout functionality.

### Public Features
- Landing page with an overview of available art products.
- Gallery showcasing art items.
- Contact and feedback forms for unauthenticated users.

### Private Features
- User profile management.
- Product management (CRUD operations) for admins and staff.
- Review management for staff and admins.
- Role-specific dashboards for admins and staff.

### Admin Features
- Full CRUD operations for all models.
- Custom admin interface with filters and search.
- Role and permission management.

### Staff Features
- Limited CRUD permissions for managing reviews and products.
- Staff-specific dashboard for role-specific functionality.

---

## Technology Stack
- **Backend**: Django Framework
- **Frontend**: Custom HTML/CSS with Django Template Engine
- **Database**: SQLite (configurable for PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- Pip (Python package manager)
- Git (optional, for cloning the repository)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd minima_art
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Public pages: [http://localhost:8000/](http://localhost:8000/)
   - Admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Usage Guide

### Roles and Permissions
- **Admin**: Full access to all features, including user and role management.
- **Staff**: Limited permissions for managing reviews and products.
- **Authenticated Users**: Access to private sections like user profiles.
- **Unauthenticated Users**: Access to public pages such as the gallery and feedback forms.

### Key URLs
- Home: `/`
- Feedback: `/feedback/`
- Gallery: `/gallery/`
- Products: `/products/`
- Staff Dashboard: `/users/staff-dashboard/`

---

## Contribution

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with descriptive messages.
4. Push the branch and create a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For inquiries or support, contact pavel.kolew@gmail.com.

