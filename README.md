
# SwipeTalk-BlogApp

This is a simple blog application built with Flask and SQLAlchemy. Users can register, log in, create blog posts, edit them, and delete them. The application also features user authentication using `Flask-Login`.

## Features
- User registration and login functionality
- Blog post creation, editing, and deletion
- View all blog posts
- Authentication system with `Flask-Login`
- SQLite database for storing users and blog posts
- Flash messages for feedback on user actions

## Technologies Used
- **Flask**: A lightweight web framework for Python.
- **SQLAlchemy**: An ORM for managing the SQLite database.
- **Flask-Login**: User session management for login/logout.
- **HTML/CSS**: For the front-end templates.

## Prerequisites
To run this application, you need to have Python installed on your system along with the following libraries:

- Flask
- Flask-SQLAlchemy
- Flask-Login

You can install the dependencies by running the following command:

```bash
pip install flask flask-sqlalchemy flask-login
```

## Database Setup
The application uses SQLite as the database. To initialize the database, run the following commands in the Python shell:

``` python
from app import db
db.create_all()
```

This will create the \`login.db\` file with the necessary tables for users and blog posts.

## File Structure

```
├── app.py            # Main application file
├── login.db          # SQLite database file (auto-created after running the app)
├── templates         # HTML files for rendering views
│   ├── home.html     # Homepage displaying all blog posts
│   ├── login.html    # User login page
│   ├── register.html # User registration page
│   ├── blog.html     # Blog creation page
│   ├── blog_detail.html # Blog details page
│   ├── edit.html     # Blog editing page
└── static            # Directory for static files like CSS/JavaScript (if used)
```

## How to Run

1. Clone this repository to your local machine.
2. Install the required dependencies using:

 ``` bash
   pip install -r requirements.txt
```

3. Initialize the database by running the following commands in the Python shell:

```python
   from app import db
   db.create_all()
```

4. Run the Flask application using:

```bash
   python app.py
```

5. Visit \`http://127.0.0.1:5000/\` in your browser to access the application.

## Routes

- \`/\` : Home page displaying all blog posts.
- \`/register\` : User registration page.
- \`/login\` : User login page.
- \`/logout\` : Logs the user out.
- \`/blogpost\` : Page for creating a new blog post.
- \`/blog_detail/<int:blog_id>\` : View details of a specific blog post.
- \`/edit/<int:blog_id>\` : Edit a blog post.
- \`/delete/<int:blog_id>\` : Delete a blog post.

## User Authentication

- Users can register and log in using their credentials. 
- The application uses the \`Flask-Login\` extension to manage user sessions. 
- A registered user can create, edit, or delete their blog posts after logging in.

## Flash Messages

Flash messages are used to notify users about the status of their actions such as successful registration, login, blog creation, editing, or deletion.

