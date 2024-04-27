# quote-management-system
Project Structure:
quotes_project: Django project directory containing project settings.
quotes: Django app directory containing models, serializers, views, URLs, and tests.
models.py: Defines the database models for Quote and Author.
serializers.py: Contains serializers to convert model instances to JSON format.
views.py: Defines API views for CRUD operations on quotes.
urls.py: Defines URL patterns to map API endpoints to views.
tests.py: Contains test cases for testing the API endpoints.
migrations: Directory containing database migration files.
admin.py: Optionally register models for administration.
API Endpoints:
GET /api/quotes/: Retrieves a list of all quotes.
POST /api/quotes/: Creates a new quote.
GET /api/quotes/<quote_id>/: Retrieves a specific quote by ID.
PUT /api/quotes/<quote_id>/: Updates an existing quote.
DELETE /api/quotes/<quote_id>/: Deletes a quote by ID.
Database Schema:
Author:
id (Primary Key)
name (CharField)
date_of_birth (DateField)
Quote:
id (Primary Key)
text (TextField)
author (Foreign Key to Author)
source (CharField, optional)
creation_date (DateTimeField)
Important Design Decisions:
Used SQLite as the database backend for simplicity in development.
Implemented basic token-based authentication and permission classes for restricting access to certain API endpoints (not included in the code provided).
Ensured proper validation of required fields in models and serializers.
Designed API endpoints following RESTful conventions for CRUD operations.
Utilized Django REST Framework for rapid development of RESTful APIs.
Instructions for Setting Up and Running the Project Locally:
Clone the repository containing the project code.
Navigate to the project directory in your terminal.
Create a virtual environment and activate it (optional but recommended).
Install dependencies listed in the requirements.txt file using pip: pip install -r requirements.txt.
Apply database migrations: python manage.py migrate.
Run the development server: python manage.py runserver.
Access the API endpoints using a tool like Postman or cURL at http://localhost:8000/api/quotes/
