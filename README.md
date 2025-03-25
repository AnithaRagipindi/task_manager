# Task Management API

## Setup Instructions
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create .env file with:
    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Start server: `python manage.py runserver`

## API Endpoints
- POST /api/tasks/create/ - Create a new task
- PUT /api/tasks/<task_id>/assign/ - Assign task to users
- GET /api/users/<user_id>/tasks/ - Get user's tasks