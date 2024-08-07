# Django Task Tracker

**Task Tracker** is a web application built with Django that helps users organize and manage their tasks. It provides a simple and intuitive interface for creating, updating, and tracking tasks, and is fully developed using Django and its templating system.

## Features

- **User Authentication**: Secure login and registration.
- **Task Management**: Create, update, delete, and view tasks.
- **Task Categories**: Organize tasks into different categories.
- **Due Dates**: Set due dates for tasks and view tasks by due date.
- **Task Status**: Mark tasks as completed or pending.
- **Responsive Design**: Accessible and usable on various devices.

## Requirements

- **Python 3.8** (or higher)
- **Django 4.x** (or higher)

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/angrezichatterbox/Django-TaskTracker/
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Django-TaskTracker
   ```

3. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage

### Accessing the Application

- **Home Page**: Visit `http://127.0.0.1:8000/` to view and manage tasks.
- **Login**: Access the login page at `http://127.0.0.1:8000/accounts/login/`.
- **Register**: Create a new account at `http://127.0.0.1:8000/accounts/register/`.

### Managing Tasks

- **Create a Task**: Navigate to the task creation page and fill out the form with task details.
- **Update a Task**: Click on a task to edit its details.
- **Delete a Task**: Click the delete button next to the task to remove it.
- **View Tasks**: View tasks by their due dates or categories on the main page.

## Contributing

Contributions are welcome! To contribute, please fork the repository and submit a pull request. For significant changes, please open an issue to discuss the changes first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact [Me!!](mailto:gouthammohanraj@gmail.com).

---
