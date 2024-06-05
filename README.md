TaskVault


Overview:

TaskVault is a robust and user-friendly task management application designed to help users efficiently manage their tasks. The project utilizes Flask for the backend, MySQL for the database, and a responsive frontend to create a seamless user experience. Whether you need to create, update, delete, or mark tasks as completed, TaskVault has got you covered.

Features:

User Authentication: Secure user registration and login.
Task Management: Create, edit, delete, and mark tasks as completed.
Due Dates: Set and manage due dates for your tasks.
Task Descriptions: Add detailed descriptions to each task.
Responsive Design: Optimized for use on various devices.

Important Files:

 app.py: The main application file that initializes the Flask app and configures the database.

 config.py: Contains configuration settings for the application.

 models.py: Defines the database models, including the User and Task models.

 routes.py: Contains the route definitions for the application, including user authentication and task management routes.

 static/: Contains css and js directories for static files like:
   - user_tasks.css: Styles for the task management pages.
   - user_tasks.js: JavaScript for handling task management interactions on the client side.

 templates/: Contains HTML templates fo the application
   - landing_page.html: The landing page of the app
   - user_tasks.html: Th page for displaying tasks for the user

 instance: Contains the SQLite databas file (if using SQLite)

Installation:
 To get started with TaskVault, follow these steps:
   1. Clone the repository:
        - git clone https://github.com/osamanazar47/TaskVault.git
		- cd TaskVault
   2. Create and activate a virtual enviroment:
        - python -m venv venv
		- source venv/bin/activate  # On Windows use `venv\Scripts\activate
   3. Install the dependencis:
        - pip install -r requirments.txt

Set up the database:
   - Update the config.py file with your MySQL database configuration.
   - Initialize the database:
       flask db upgrade
   - Run the application:
       flask run

Usage
   Register: Create a new user account.
   Login: Access your account.
   Manage Tasks: Create, edit, delete, and mark tasks as completed.
