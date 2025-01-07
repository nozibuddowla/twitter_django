# Twitter Clone

A simple Twitter clone built with Django, Bootstrap, and custom user authentication. This project allows users to create, edit, delete, and search tweets, as well as register and log in to their accounts.

## Live Demo

[Live Demo](https://twitter-django.onrender.com/)

## Features

- **User Registration**: Users can create an account with a username, email, and password.
- **User  Authentication**: Users can log in and log out securely.
- **Tweet Management**: Users can create, edit, and delete their tweets.
- **Search Functionality**: Users can search for tweets by keywords, regardless of case.
- **Responsive Design**: The application is built using Bootstrap for a mobile-friendly interface.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default for development)
- **Version Control**: Git

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nozibuddowla/twitter_django.git

2. **Navigate to the project directory**:
    ```bash
    cd twitter_django

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Apply migrations**:
    ```bash
    python manage.py migrate

5. **Start the server**:
    ```bash
    python manage.py runserver

## Usage

- Register a new user or log in with an existing account.
- Create, edit, and delete tweets.
- Use the search bar to find tweets.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### **3. Test Your Application**
Run your application and test all features to ensure everything works as expected:
- User registration and login
- Creating, editing, deleting, and searching tweets
- Edge cases like invalid inputs or no search results

---

### **4. Lint Your Code**
Ensure your code follows best practices and is free of syntax errors.
- Use `flake8` for Python linting:
  ```bash
  pip install flake8
  flake8 .
