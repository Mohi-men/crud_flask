# Task Smash 2.0

A simple Flask-based task management (CRUD) web application.

## Features

- Add, edit, and delete tasks
- Tasks stored in a SQLite database
- Styled with SCSS/CSS
- Uses Flask, Flask-SQLAlchemy, Flask-Scss

## Setup

1. **Clone the repository**  
   ```sh
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```sh
   flask run
   ```
   or  
   ```sh
   python app.py
   ```

5. **Open in browser**  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

- `app.py` - Main Flask application
- `model/Task.py` - Database model and CRUD functions
- `templates/` - HTML templates
- `static/css/` - CSS/SCSS files
- `instance/database.db