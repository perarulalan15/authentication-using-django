# Django Authentication System

This project is a Django-based authentication system designed to provide secure user authentication and authorization functionalities for web applications. It includes features such as user registration, login, logout and user profile management.

## Features

- User registration with email verification
- User login/logout functionality
- User profile management
- Session management for user authentication

## Installation

1. Clone the repository:
   ```bash
   https://github.com/perarulalan15/authentication-using-django.git
2. Navigate into the project directory:
   ```bash
   cd authentication-using-django

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Apply database migrations:
   ```bash
   python manage.py migrate

6. Access the application at [http://localhost:8000](http://localhost:8000)

## Configuration

- **Database Configuration**: Update the database settings in `settings.py` according to your database setup.
- **Email Configuration**: Configure email settings in `settings.py` for features like user registration email verification and password reset emails.
- **Customization**: Customize templates, views, and forms according to your requirements.

## Usage

1. **User Registration**: Users can register using a valid email address. After registration, they receive an email with a verification link.
2. **Login/Logout**: Registered users can log in using their credentials. They can also log out after their session.
3. **User Profile Management**: Users can update their profile information, including username, email address, and password.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
