# Todo List

A simple web application for managing daily tasks and organizing them with tags.

The project is built with Django and provides basic task management functionality, including creating, editing, deleting, and completing tasks, as well as setting deadlines and assigning tags.

## Features

* Create new tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed or not completed
* Set optional deadlines
* Create, edit, and delete tags
* Assign multiple tags to a task
* Display active tasks before completed tasks
* Sort tasks by creation date

## Technologies

* Python
* Django 6.0.7
* HTML
* CSS
* Bootstrap
* SQLite

## Requirements

Before running the project, make sure you have installed:

* Python 3.12, 3.13, or 3.14
* Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vladiukdaria-debug/todo-list.git
```

### 2. Navigate to the project directory

```bash
cd todo-list
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Set environment variables

The project expects `SECRET_KEY` and `DEBUG` environment variables.

#### Windows PowerShell

```powershell
$env:SECRET_KEY="your-development-secret-key"
$env:DEBUG="True"
```

#### Windows Command Prompt

```cmd
set SECRET_KEY=your-development-secret-key
set DEBUG=True
```

#### macOS / Linux

```bash
export SECRET_KEY="your-development-secret-key"
export DEBUG="True"
```

> Use a secure secret key and disable debug mode in a production environment.

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Usage

After starting the application, you can:

1. Create a new task and specify its content.
2. Set an optional deadline.
3. Assign one or more tags to the task.
4. Edit or delete existing tasks.
5. Mark tasks as completed or return them to the active state.
6. Create, edit, and delete tags on the tags page.

## Data Models

### Task

Each task contains:

* `content` — task description
* `created_at` — date and time when the task was created
* `deadline` — optional task deadline
* `is_done` — task completion status
* `tags` — tags assigned to the task

### Tag

Each tag contains:

* `name` — unique tag name

A task can have multiple tags, and each tag can be assigned to multiple tasks.

## Project Structure

```text
todo-list/
├── config/              # Django project configuration
├── tasks/               # Main application with tasks and tags
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```

## Main URLs

| URL                   | Description                   |
| --------------------- | ----------------------------- |
| `/`                   | List of tasks                 |
| `/tasks/create/`      | Create a task                 |
| `/tasks/<id>/update/` | Update a task                 |
| `/tasks/<id>/delete/` | Delete a task                 |
| `/tasks/<id>/toggle/` | Change task completion status |
| `/tags/`              | List of tags                  |
| `/tags/create/`       | Create a tag                  |
| `/tags/<id>/update/`  | Update a tag                  |
| `/tags/<id>/delete/`  | Delete a tag                  |

## Author

**vladiukdaria-debug**

## Project Status

The project was created for educational purposes and demonstrates basic CRUD operations, Django class-based views, forms, model relationships, and task management functionality.
