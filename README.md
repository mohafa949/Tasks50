# Tasks50
#### Video Demo:  https://youtu.be/mxdY6kOyPKc
#### Description:
Tasks50 is a web application designed to help users manage their tasks effectively. It allows users to add tasks, mark them as completed, and review their progress. This application is built with Flask and aims to provide a simple yet efficient solution for task management. The project is structured into four main sections:

## 1. Static Folder:
The static folder contains all the static files used for styling the application. It includes a CSS file, styles.css, which defines the design elements such as fonts, colors, hover effects, and overall layout. This file ensures a consistent and visually appealing user interface throughout the application.

## 2. Templates Folder
The templates folder contains the HTML and JavaScript files responsible for the application's frontend. Each file serves a specific purpose:

### layout.html:
 This is the base template used by all other HTML files. It includes shared components like the navigation header, which allows users to access different routes of the web application. It also contains the JavaScript code that enhances the app's interactivity.
### register.html: 
This page allows new users to create an account. Users must enter a unique username (one not already in use) and a password that is at least 8 characters long for security. After confirming their password, users are added to the database, ensuring that only valid registrations are accepted.
### login.html: 
This page enables registered users to log in by entering their username and password. Upon successful authentication, users are redirected to the "Add Task" page, where they can start managing their tasks.
### index.html: 
Also referred to as the "Add Task" page, this is the main page of the application. Users can add tasks by entering them into input fields generated dynamically using loops. Upon submitting the form, the tasks are saved to the database, and the user is redirected to the "Tasks" page.
### tasks.html: 
This page displays the tasks added by the user. It provides a checklist where users can mark tasks as completed. Once submitted, the completed tasks are updated in the database.
### checked.html: 
This page shows a table of completed tasks along with the dates they were marked as finished. It helps users keep track of their accomplishments.
### 3. finalproject.db
The finalproject.db file is an SQLite database that stores all the data required for the application. It contains two primary tables:

users table: This table stores user information, including user IDs, usernames, and their hashed passwords. Storing hashed passwords ensures that sensitive user data remains secure.
tasks tables: For each user, a unique table named tasks_<user_id> is created. This table stores all tasks added by the user, whether they are completed, and the dates on which they were marked as completed.
This database structure ensures efficient data storage and retrieval, enabling smooth functionality across the application.

## 4. app.py
The app.py file is the backbone of the application. It contains all the route functions and logic that make the application dynamic and interactive. It imports essential libraries and includes a login_required() function to ensure that only authenticated users can access specific routes. The key routes include:

### / (index route):

GET method: When users access this route, a task table is created for them if it doesn’t already exist. The function then retrieves tasks from the database and displays them on the "Add Task" page.
POST method: When users submit tasks via the form, the function loops through the tasks in request.form.getlist('tasks') and adds them to the database. Users are then redirected to the /tasks route.
### /task (tasks route):

GET method: Retrieves tasks that are not yet marked as completed and displays them on the "Tasks" page as a checklist.
POST method: Updates the database with the tasks marked as completed by the user. These completed tasks are then displayed on the "Checked Tasks" page.
### /checked:
This route renders the checked.html template and displays a table of tasks that have been marked as completed, along with their completion dates.

### /register: 
This route handles user registration. It includes multiple checks to ensure that the username is unique, the password meets the minimum length requirement of 8 characters, and the password confirmation matches. If all conditions are met, the password is hashed using generate_password_hash(), and the user is added to the database.

### /login:
This route authenticates users by checking if their username exists in the database and if their entered password matches the hashed password using check_password_hash(). If authentication is successful, the user ID is stored in the session dictionary to track the logged-in user.

### /logout:
 Clears the session dictionary to log out the current user, allowing another user to log in.
#
Overall, Tasks50 is a robust and user-friendly task management application that leverages Flask to provide a dynamic and efficient experience. By combining a well-structured database, intuitive frontend design, and secure authentication mechanisms, it ensures a seamless and secure task management process for users.