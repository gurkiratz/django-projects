# Books App - Django

This is a simple `Books` application built with Django and Django REST Framework that allows users to manage and view books. The app includes both a web interface for managing books and an API to retrieve book data.

## Features
- User authentication (login, logout, and registration)
- Book management (Add, Edit, Delete books)
- Book API using Django REST Framework
- Home page displaying all books
- Book detail page with edit and delete options for the creator
- API routes to list books and retrieve a single book by its ID

## Installation

### Requirements
- Python 3.x
- Django
- Django REST Framework

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/books-app.git
    cd books-app
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

   - If `requirements.txt` is not available, manually install the necessary packages:

     ```bash
     pip install django djangorestframework
     ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Running the App
1. Visit `http://127.0.0.1:8000/` in your browser to access the homepage.
2. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and books (use the superuser credentials you created).
3. Use the Book API at the following endpoints:
    - `GET /api/routes/`: Get a list of all available API routes
    - `GET /api/books/`: Get a list of all books
    - `GET /api/books/<id>/`: Get a specific book by its ID

## API Endpoints

### `GET /api/routes/`
Returns a list of available API routes.

**Response:**

```json
[
  "GET /api/books/",
  "GET /api/books/<id>/"
]
```

### `GET /api/books/`
Returns a list of all books.


**Response:**

```json
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "year": 2023,
    "rating": 4.5,
    "description": "A short description of the book.",
    "created_by": 1
  },
]
```

### `GET /api/books/<id>/`

Returns details of a specific book identified by its `id`.

**Response:**

```json
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "year": 2023,
  "rating": 4.5,
  "description": "A short description of the book.",
  "created_by": 1
}
```

## Project Structure

```bash
books-app/
│
├── books/                # Main app for the project
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates for the frontend
│   │   ├── add_book.html
│   │   ├── edit_book.html
│   │   ├── homepage.html
│   │   ├── layout.html
│   │   ├── navbar.html
│   │   └── book_detail.html
│   ├── models.py         # Book model and database schema
│   ├── serializers.py    # Serializers for the API
│   ├── urls.py           # URL routes for the app
│   ├── views.py          # Views for both web and API
│   └── forms.py          # Forms for adding/editing books
│
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies (Django, DRF)
```