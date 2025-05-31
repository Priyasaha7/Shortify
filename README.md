# We are making a url shortner website 

# 🔗 Flask URL Shortener

A simple URL shortener built using **Python Flask**, **SQLite**, and **SQLAlchemy**. This app lets users create short links from long URLs — optionally with a custom alias.


## 📁 Project Structure

URLshortener/
├── .env # Environment variables (do not commit)
├── .env.sample # Sample .env file for reference
├── app.py # Main Flask app
├── config.py # App configuration
├── models.py # Database models (SQLAlchemy)
├── routes.py # Routes and logic
├── requirements.txt # Python dependencies
├── README.md # Documentation
└── templates/
└── index.html # HTML frontend


# Create Folder & Virtual Environment

```bash
# Go to desired drive
    D:
    mkdir URLshortener
    cd URLshortener

# Create and activate virtual environment
    python -m venv .venv

# Activate on Windows
    .venv\Scripts\activate

# Or on macOS/Linux
    source .venv/bin/activate

# Create Required Files & Folders
    bash
    Copy
    Edit
# Create project files
    touch .env .env.sample app.py config.py routes.py models.py README.md requirements.txt

# Create templates folder and HTML file
    mkdir templates
    cd templates
    touch index.html
    cd ..

# Install Required Packages
    bash
    Copy
    Edit
    pip install flask flask_sqlalchemy python-dotenv
    Then freeze dependencies:

    bash
    Copy
    Edit
    pip freeze > requirements.txt

# Setup Environment Variables
    In your .env:
    env
    Copy
    Edit
    FLASK_APP=app.py
    FLASK_ENV=development
    DATABASE_URL=sqlite:///urls.db
    SECRET_KEY=your_secret_key_here
    In .env.sample (template for others):

    env
    Copy
    Edit
    FLASK_APP=
    FLASK_ENV=
    DATABASE_URL=
    SECRET_KEY=

#How It Works
    User submits a long URL.
    App generates a short code (or uses a custom alias).
    The long URL is stored with the code in the database.
    Visiting the short URL redirects to the original.

#Database Setup
    Using SQLite via SQLAlchemy. To initialize:
    python
    Copy
    Edit
# In Python shell or setup script
from app import app
from models import db

with app.app_context():
    db.create_all()
🖥️ Example HTML (templates/index.html)

    <!DOCTYPE html>
    <html>
    <head><title>URL Shortener</title></head>
    <body>
        <h1>Shorten Your URL</h1>
        <form method="POST" action="/">
        <input type="url" name="long_url" placeholder="Enter long URL" required>
        <input type="text" name="custom_alias" placeholder="Custom alias (optional)">
        <button type="submit">Shorten</button>
        </form>
    </body>
    </html>

✨ Features To Add
✅ Custom aliases
📊 Click tracking
⏳ Expiry time for links
🔐 User login & authentication
🌐 Public API endpoints
🧪 Unit tests with pytest
📦 Run the App
    bash
    Copy
    Edit
    flask run
    Visit: http://127.0.0.1:5000

📌 .gitignore Suggestions
    gitignore
    Copy
    Edit
    .venv/
    .env
    __pycache__/
    *.pyc
    *.db

 Acknowledgements
    Flask
    SQLAlchemy
    python-dotenv

