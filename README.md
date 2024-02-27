# Flask-RESTful Todo API

This small project is a simple yet powerful demonstration of a RESTful API developed with Flask and Flask-RESTful, 
designed to manage a to-do list. It showcases the fundamental principles of RESTful API design, including stateless 
client-server architecture, uniform interface, and resource manipulation through HTTP methods.

## Features
- CRUD Operations: Supports Create, Read, Update, and Delete operations on to-do items.
- In-Memory Storage: Utilizes a Python dictionary for in-memory data storage, making it easy to test and understand the 
API's functionality without the need for external databases.
- Error Handling: Implements basic error handling, returning appropriate HTTP status codes and messages for different 
scenarios, such as resource not found.

## Getting Started
Below are the instructions to set up and run the API locally.

## Prerequisites
- Python 3.x
- Flask
- Flask-RESTful

## Installation
First, clone the repository to your local machine:

```
git clone https://github.com/yourusername/flask-restful-todo-api.git
cd flask-restful-todo-api
```

Then, create a virtual environment and activate it:

- ### Windows

```commandline
python -m venv env
.\env\Scripts\activate
```

- ### macOS/Linux
```commandline
python3 -m venv env
source env/bin/activate
```

Install the required packages:

```commandline
pip install flask flask-restful
```


## Running the Application

Start the Flask application with:
```commandline
python app.py
```

The API will be accessible at http://127.0.0.1:5000/.


### Using cURL
- Creating a New Todo Item
To create (or update) a todo item with a specific todo_id, you can use the PUT method. In this example, we're creating 
a todo item with the id todo1 and data "Learn Python".
```commandline
curl -X PUT http://localhost:5000/todo1 -d "data=Learn Python" -H "Content-Type: application/x-www-form-urlencoded"
```

- Retrieving a Todo Item
To retrieve an existing todo item by its todo_id, use the GET method. Here's how to retrieve todo1:
```commandline
curl http://localhost:5000/todo1
```

- Deleting a Todo Item
To delete an existing todo item, use the DELETE method. Here's the command to delete todo1:
```commandline
curl -X DELETE http://localhost:5000/todo1
```


### API Endpoints

- #### GET /<todo_id>: Retrieve a specific to-do item by ID.
- #### PUT /<todo_id>: Update (or create) a to-do item with the given ID.
- #### DELETE /<todo_id>: Remove a to-do item by its ID.


## Contributing
Contributions are welcome! Please feel free to submit pull requests, report bugs, and suggest improvements.
