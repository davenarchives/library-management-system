import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

class Library:
    def __init__(self, host, database, user, password):
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def add_book(self, BookTitle, BorrowerName, PhoneNumber, DateBorrowed):
        try:
            if not all((BookTitle, BorrowerName, PhoneNumber)):
                messagebox.showerror("Error", "Please fill in all required fields.")
                return

            self.cursor.execute("SELECT * FROM books WHERE BookTitle = %s AND BorrowerName = %s AND PhoneNumber = %s", (BookTitle, BorrowerName, PhoneNumber))
            existing_record = self.cursor.fetchone()
            if existing_record:
                messagebox.showinfo("Info", "Data already recorded.")
            else:
                self.cursor.execute("INSERT INTO books (BookTitle, BorrowerName, PhoneNumber, DateBorrowed) VALUES (%s, %s, %s, %s)", (BookTitle, BorrowerName, PhoneNumber, DateBorrowed))
                self.connection.commit()
                messagebox.showinfo("Success", "Data recorded successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add book: {e}")

    def display_borrowed_books(self):
        try:
            self.cursor.execute("SELECT BookTitle, BorrowerName, PhoneNumber, DateBorrowed FROM books WHERE BorrowerName IS NOT NULL")
            borrowed_books = self.cursor.fetchall()
            if not borrowed_books:
                messagebox.showinfo("Info", "No books currently borrowed.")
            else:
                top = Toplevel()
                top.title("Borrowed Books")
                top.geometry("1100x300")
                top.configure(bg="#f5f5f5")

                header_label = Label(top, text="Borrowed Books List", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
                header_label.pack(pady=10)

                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview", font=("Helvetica", 10), rowheight=25, background="#f5f5f5", fieldbackground="#f5f5f5")
                style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"), background="#e1e1e1")
                style.map('Treeview', background=[('selected', '#2a8dff')], foreground=[('selected', 'white')])

                tree_frame = Frame(top, bg="#f5f5f5")
                tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)

                tree = ttk.Treeview(tree_frame, columns=("Title", "Borrower", "Phone Number", "DateBorrowed"), show="headings", yscrollcommand=tree_scroll.set)
                tree.pack(fill=BOTH, expand=True)

                tree_scroll.config(command=tree.yview)

                tree.heading("Title", text="Book Title")
                tree.heading("Borrower", text="Name of the Borrower")
                tree.heading("Phone Number", text="Phone Number")
                tree.heading("DateBorrowed", text="Date Borrowed")

                for book in borrowed_books:
                    tree.insert("", "end", values=book)

                close_button = Button(top, text="Close", command=top.destroy, font=("Helvetica", 10), bg="#e1e1e1")
                close_button.pack(pady=10)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to display borrowed books: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

def main():
    root = Tk()
    root.title("Library Management System")

    gui_title = Label(root, text="Library System GUI", font=("Helvetica", "16", "bold"), fg="blue")
    gui_title.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="w")

    library = Library("localhost", "library", "root", "09776376825")

    sample_books = [
        "",
        "1984, George Orwell (1949)",
        "A Brief History of Time, Stephen Hawking (1988)",
        "A Song of Ice and Fire, George R.R. Martin (1996)",
        "Animal Farm, George Orwell (1945)",
        "Brave New World, Aldous Huxley (1932)",
        "Bleach, Tite Kubo (2001)",
        "Crime and Punishment, Fyodor Dostoevsky (1866)",
        "Don Quixote, Miguel de Cervantes (1605)",
        "Dune, Frank Herbert (1965)",
        "Frankenstein, Mary Shelley (1818)",
        "Hamlet, William Shakespeare (1603)",
        "Harry Potter, J.K. Rowling (1997-2007)",
        "In Search of Lost Time, Marcel Prous (1913)",
        "Lord of the Rings, Tolkien (1954-1955)",
        "No Longer Human, Osamu Dazai (1948)",
        "One Piece, Eiichiro Oda (1999)",
        "Pride and Prejudice, Jane Austen (1813)",
        "The Catcher in the Rye, J.D. Salinger (1951)",
        "The Great Gatsby, Scott Fitzgerald (1925)",
        "The Hobbit, J.R.R. Tolkien (1937)",
        "The Hunger Games, Suzanne Collins (2008-2010)",
        "The Kite Runner, Khaled Hosseini (2003)",
        "The Shining, Stephen King (1977)",
        "To Kill a Mockingbird, Harper Lee (1960)",
        "Ulysses, James Joyce (1922)",
        "War and Peace, Leo Tolstoy (1869)",
        "Wuthering Heights, Emily Bronte (1847)"
    ]

    def add_book():
        title = book_choice.get()
        borrower_name = borrower_name_entry.get()
        phone_number = phone_number_entry.get()
        date_borrowed = datetime.now().strftime('%Y-%m-%d')
        library.add_book(title, borrower_name, phone_number, date_borrowed)

    def display_borrowed_books():
        library.display_borrowed_books()

    def on_closing():
        library.close_connection()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    title_label = Label(root, text="Type/Select Book:", font=("Arial", 12))
    title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    book_choice = ttk.Combobox(root, values=sample_books, width=50)
    book_choice.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
    book_choice.current(0)

    borrower_name_label = Label(root, text="Name of Borrower:", font=("Arial", 12))
    borrower_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    def on_borrower_name_entry_click(event):
        if borrower_name_entry.get() == "Surname, First Name MI":
            borrower_name_entry.delete(0, "end")
            borrower_name_entry.config(fg='black')

    def on_borrower_name_entry_leave(event):
        if not borrower_name_entry.get():
            borrower_name_entry.insert(0, "Surname, First Name MI")
            borrower_name_entry.config(fg='grey')

    borrower_name_entry = Entry(root, width=50)
    borrower_name_entry.insert(0, "Surname, First Name MI")
    borrower_name_entry.config(fg='grey')
    borrower_name_entry.bind("<FocusIn>", on_borrower_name_entry_click)
    borrower_name_entry.bind("<FocusOut>", on_borrower_name_entry_leave)
    borrower_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    phone_number_label = Label(root, text="Phone Number:", font=("Arial", 12))
    phone_number_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    def on_phone_number_entry_click(event):
        if phone_number_entry.get() == "ex. 09XX-XXXX-XXX":
            phone_number_entry.delete(0, "end")
            phone_number_entry.config(fg='black')

    def on_phone_number_entry_leave(event):
        if not phone_number_entry.get():
            phone_number_entry.insert(0, "ex. 09XX-XXXX-XXX")
            phone_number_entry.config(fg='grey')

    phone_number_entry = Entry(root, width=50)
    phone_number_entry.insert(0, "ex. 09XX-XXXX-XXX")
    phone_number_entry.config(fg='grey')
    phone_number_entry.bind("<FocusIn>", on_phone_number_entry_click)
    phone_number_entry.bind("<FocusOut>", on_phone_number_entry_leave)
    phone_number_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    display_borrowed_books_button = Button(root, text="Display Data", command=display_borrowed_books, font=("Arial", 10))
    display_borrowed_books_button.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

    add_book_button = Button(root, text="Borrow", command=add_book, font=("Arial", 10))
    add_book_button.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    main()
