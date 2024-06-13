# 📚 PagePilot: Library Management System

Welcome to **PagePilot**, the next-generation library management system that brings the power of digital cataloging and user management to your fingertips. Designed with simplicity and efficiency in mind, PagePilot provides a seamless experience for librarians and users alike.

## 🌟 Features

- **📖 Book Management**: Effortlessly manage your library's book inventory with options to add, update, delete, list, and search for books.
- **👤 User Management**: Keep track of your library's users with comprehensive user management capabilities.
- **🔄 Transaction Handling**: Simplify the process of issuing and returning books with our intuitive transaction management system.
- **🔍 Search Functionality**: Quickly find books and users with our advanced search options.
- **📈 Reporting**: Generate reports on book availability and user activity with just a few clicks.

## 🚀 Getting Started

Follow these instructions to get PagePilot running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- Django 2.2 or higher

### Installation

Get your development environment up and running with these simple steps:

1. **Clone the Repository**:
   ```shell
   git clone https://github.com/yourusername/PagePilot.git

   ```

2. **Navigate to Project Directory**:
   ```shell
   cd PagePilot

   ```

3. **Set Up a Virtual Environment and Install Dependencies**:
   ```shell
   pip install -r requirements.txt

   ```

4. **Fire Up the Server**:
   ```shell
   python manage.py runserver

   ```

5. **Visit Your Application and Test Using Postman**:
   ```shell
   http://127.0.0.1:8000/

   ```

### 📜 URL Patterns

- `/ensure`: A quick health check to ensure the system is operational.
- `/books/list`: View a list of all books in the library.
- `/books/add`: Add a new book to the collection.
- `/books/update`: Update details of an existing book.
- `/books/delete`: Remove a book from the library.
- `/books/search`: Find a book with specific attributes.
- `/users/list`: List all registered users.
- `/users/add`: Register a new user.
- `/users/update`: Edit user information.
- `/users/delete`: Delete a user profile.
- `/users/search`: Search for users by their attributes.
- `/issue`: Issue a book to a user.
- `/return`: Process the return of a book.


## API Endpoints

The Library Management System provides a variety of API endpoints to manage books and users efficiently. Below is a list of available endpoints and their functionalities:

### Health Check
- `GET /ensure`
  - Description: Performs a quick health check to confirm the system is operational.
  - Response: A message indicating the system's status.

### Book Management
- `GET /books/list`
  - Description: Retrieves a list of all books in the library's collection.
  - Response: A JSON array of book objects.

- `POST /books/add`
  - Description: Adds a new book to the library's collection.
  - Payload: JSON object containing book details (title, author, isbn, availability).
  - Response: Confirmation message with the added book details.

- `POST /books/update`
  - Description: Updates the details of an existing book in the library.
  - Payload: JSON object containing updated book details. (query, kwargs)
  - Response: Confirmation message with the updated book details.

- `POST /books/delete`
  - Description: Removes a book from the library's collection.
  - Payload: JSON object containing the book's identifier (query).
  - Response: Confirmation message indicating successful deletion.

- `POST /books/search`
  - Description: Searches for books with specific attributes (e.g., title, author).
  - Query Parameters: Search criteria such as title, author, or ISBN.
  - Response: A JSON array of book objects matching the search criteria.

### User Management
- `GET /users/list`
  - Description: Lists all registered users of the library.
  - Response: A JSON array of user objects.

- `POST /users/add`
  - Description: Registers a new user to the library.
  - Payload: JSON object containing user details (name, user_id, phone, email).
  - Response: Confirmation message with the registered user details.

- `POST /users/update`
  - Description: Edits the information of an existing user.
  - Payload: JSON object containing updated user details. (query, kwargs)
  - Response: Confirmation message with the updated user details.

- `POST /users/delete`
  - Description: Deletes a user profile from the library's records.
  - Payload: JSON object containing the user's identifier (query).
  - Response: Confirmation message indicating successful deletion.

- `POST /users/search`
  - Description: Searches for users by their attributes (e.g., name, user ID).
  - Query Parameters: Search criteria such as name or user ID.
  - Response: A JSON array of user objects matching the search criteria.

### Transaction Management
- `POST /issue`
  - Description: Issues a book to a user, marking it as checked out.
  - Payload: JSON object containing the user's identifier and the book's ISBN.
  - Response: Confirmation message with the issue details.

- `POST /return`
  - Description: Processes the return of a book, marking it as available again.
  - Payload: JSON object containing the user's identifier and the book's ISBN.
  - Response: Confirmation message with the return details.
