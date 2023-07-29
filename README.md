# ManSkiller - Portfolio Management Application

![image](https://github.com/Manoj890880/man-skiller/assets/112793753/9bc9e731-a1ed-4437-a395-e365a7b0f3b5)


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Entities](#entities)
- [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Technology Stack](#technology-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Introduction

ManSkiller is an advanced and versatile web application designed for efficient project portfolio management. It serves as a comprehensive solution for businesses and individuals to manage their projects, tasks, and resources effectively, empowering them to succeed in project delivery.

The application offers a seamless user experience, combining the power of Vue.js for a responsive frontend and Python Flask for a robust backend. With MongoDB as the database, ManSkiller ensures reliable and scalable data management.

---

## Features

- **Portfolio Manager and Project Management**: Easily manage Portfolio Managers and their Projects using CRUD operations. Create clear associations between multiple Projects and Portfolio Managers.

- **Task Management**: Stay organized by creating, updating, and tracking tasks associated with specific Projects.

- **Resource Management**: Efficiently manage project resources by linking them to appropriate Tasks and assigning responsible Portfolio Managers. Resources can be flexibly assigned to multiple tasks.

- **Project Listing**: Access a project listing page with pagination, filtering (by Status and Portfolio Manager), and sorting (by Status and Start Date) features for convenient project navigation.

---

## Entities

### Portfolio Manager

A Portfolio Manager plays a crucial role in project oversight. Their profile includes essential information:
- **Name**: The name of the Portfolio Manager.
- **Status**: Indicates whether the Portfolio Manager is currently active or inactive.
- **Role**: The role of the Portfolio Manager (Administrator or Viewer).
- **Bio**: A concise bio or description of the Portfolio Manager.
- **Start Date**: The date when the Portfolio Manager started their role.

### Project

Projects are the core element of the application. They include the following fields:
- **Project Name**: The name of the project.
- **Status**: The current status of the project (Planned, In Progress, or Completed).
- **Start Date**: The date when the project commenced.
- **End Date**: The date when the project was successfully completed.

### Task

Tasks represent individual activities or assignments within a project. The Task entity includes:
- **Status**: The status of the Task (To Do, In Progress, or Completed).

### Resource

Resources are essential components for completing Tasks. The Resource entity consists of:
- **Link to Task**: The Task to which the Resource is associated.
- **Link to Portfolio Manager**: The Portfolio Manager responsible for the Resource.
- **Description**: A brief description of the Resource.

---

## Entity-Relationship Diagram

![image](https://github.com/Manoj890880/man-skiller/assets/112793753/3434e6eb-46f3-4217-a87c-47dfde42667d)


---

## Technology Stack

ManSkiller leverages the following powerful technology stack:

- **Front-end**: Vue.js for an interactive and responsive user interface.
- **Back-end**: Python Flask for a robust and efficient server-side.
- **Database**: MongoDB for scalable and reliable data management.

---

## Screenshots

Here are some screenshots showcasing the user interface and functionalities of ManSkiller:

![image](https://github.com/Manoj890880/man-skiller/assets/112793753/eebc1d54-9ffa-46d4-a912-cb8d639a49d4)

![image](https://github.com/Manoj890880/man-skiller/assets/112793753/5b4eba1f-408a-4701-80ab-2a9b038a8f83)

![image](https://github.com/Manoj890880/man-skiller/assets/112793753/a63bf403-4cd5-4bb1-baae-62162c3804a8)


---

## Getting Started

To get started with ManSkiller, follow these steps:

1. Clone this repository to your local machine.
2. Install Python and MongoDB (if not already installed).
3. Set up the database and collections using the provided schema.
4. Configure the database connection in the backend (Python Flask).
5. Navigate to the "frontend" folder and run `npm install` to install frontend dependencies.
6. Start the frontend development server using `npm run serve`.
7. Navigate to the "backend" folder and set up a Python virtual environment.
8. Install backend dependencies using `pip install -r requirements.txt`.
9. Start the backend server using `python app.py`.
10. Access the application in your web browser at `http://localhost:8080`.



---

## Contributing

We warmly welcome contributions from the community to enhance ManSkiller. To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name (e.g., feature/add-new-feature).
3. Make necessary changes and commit them.
4. Push the changes to your forked repository.
5. Create a pull request to the `main` branch of this repository.

We value your insights and efforts in making ManSkiller even better!





---

## Contact

For any inquiries or support, feel free to reach out to our team at [contact@example.com](mailto:manojsahoo890880@gmail.com).

Let's make project management a delightful experience with ManSkiller!
