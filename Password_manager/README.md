# Django Password Manager

A secure, web-based password manager built with Python and Django.

## Features

- User authentication (register, login, logout)
- Store website credentials (website, username, password)
- View, create, update, and delete passwords
- Duplicate prevention: one password per website per user
- Real-time duplicate checking with suggestions
- Search functionality to quickly find passwords
- Password generator to create strong, secure passwords
- Responsive design using Bootstrap

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and navigate to http://127.0.0.1:8000/

## Usage

1. Register a new account or log in with your credentials
2. Use the "Add Password" button to store new website credentials
3. View all your passwords on the dashboard
4. Click on the "Actions" dropdown to edit or delete a password
5. Use the search bar to find specific passwords
6. Click the "Generate Strong Password" button when creating a new password to generate a secure random password

## Security Considerations

This is a basic password manager for educational purposes. For production use, consider the following enhancements:

- Enable HTTPS for all connections
- Implement password encryption at rest
- Add two-factor authentication
- Add session timeouts
- Implement a master password with strong hashing
- Regularly backup the database

## License

This project is licensed under the MIT License - see the LICENSE file for details. 