# Library Management System

This project is a simple **Library Management System** with a graphical user interface (GUI) built using Python's `tkinter` library and a MySQL database for storing and retrieving data. It allows users to record books borrowed from the library and view the list of borrowed books.

---

## Features

1. **Add a Book**: Record a borrowed book with details like the book title, borrower's name, and phone number.
2. **Display Borrowed Books**: View a list of all borrowed books in a separate window with a table layout.
3. **Persistent Storage**: Data is stored in a MySQL database, ensuring records are not lost when the application is closed.

---

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **MySQL Database**: A MySQL server should be running, and a database named `library` with a `books` table must be created.
3. **Python Libraries**: Install the required libraries using the following command:
   ```bash
   pip install mysql-connector-python
   ```

---

## Database Setup

Before running the application, set up the MySQL database:

1. Open your MySQL command-line client or a GUI tool like phpMyAdmin.
2. Run the following SQL commands to create the database and table:
   ```sql
   CREATE DATABASE library;

   USE library;

   CREATE TABLE books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       BookTitle VARCHAR(255) NOT NULL,
       BorrowerName VARCHAR(255) NOT NULL,
       PhoneNumber VARCHAR(15) NOT NULL,
       DateBorrowed DATE NOT NULL
   );
   ```

---

## How to Run

1. Clone or download the project.
2. Open the script in a Python-compatible IDE (e.g., VSCode, PyCharm) or a terminal.
3. Modify the database connection details in the `Library` class's constructor:
   ```python
   library = Library("localhost", "library", "root", "<your_password>")
   ```
4. Run the script:
   ```bash
   python script_name.py
   ```

---

## User Interface

1. **Main Window**:
   - Input fields for book title, borrower's name, and phone number.
   - Dropdown menu for selecting book titles from a predefined list.
   - Buttons for borrowing a book and displaying borrowed books.

2. **Borrowed Books Window**:
   - Displays a list of borrowed books in a tabular format.
   - Includes a "Close" button to exit the window.

---

## Code Structure

### Classes

- **`Library`**: Handles all database-related operations such as adding books and retrieving borrowed books.
  - `add_book()`: Adds a new book record to the database.
  - `display_borrowed_books()`: Opens a new window displaying all borrowed books.
  - `close_connection()`: Closes the MySQL database connection.

### Functions

- **`add_book()`**: Captures input from the GUI and passes it to the `add_book()` method of the `Library` class.
- **`display_borrowed_books()`**: Calls the `display_borrowed_books()` method to show all borrowed books.
- **`on_closing()`**: Ensures the database connection is closed before exiting the application.

### GUI Components

- **Labels and Entry Widgets**: For input fields (e.g., borrower's name, phone number).
- **Dropdown Menu**: For selecting book titles.
- **Buttons**: For actions like borrowing a book and viewing borrowed books.
- **Treeview Table**: Displays borrowed books in a structured format.

---

## Sample Book Titles

The application includes a dropdown list of sample book titles:

- *1984* by George Orwell
- *A Brief History of Time* by Stephen Hawking
- *The Great Gatsby* by F. Scott Fitzgerald
- *To Kill a Mockingbird* by Harper Lee
- ... and more.

---

## Error Handling

1. Checks for empty fields before adding a book record.
2. Displays an error message if the MySQL connection or query fails.
3. Prevents duplicate entries by checking existing records before adding new ones.

---

## License

This project is open-source and available under the MIT License.

