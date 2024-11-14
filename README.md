# Expense Tracker Web Application

## Project Overview

This project is a web-based **Expense Tracker** built using **Python** and **Flask**. The application allows users to add, view, and track their income and expenses conveniently. It uses an **SQLite** database for storing transactions and features a user-friendly interface to simplify personal financial management.

## Features

- Add Income and Expenses with categories, amounts, and descriptions.
- View all transactions with details (date, category, amount, etc.) in a table format.
- Categorize transactions into Income or Expense.
- Visualize spending through an easy-to-navigate interface.

## Project Structure

```
expense_tracker/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── database.py
│   ├── static/
│   │     └── styles.css
│   ├── templates/
│   │     ├── base.html
│   │     ├── index.html
│   │     ├── add_transaction.html
│   │     └── view_transactions.html
├── run.py
├── requirements.txt
└── README.md
```

### File Descriptions
- **app/**: Contains all the core files for the application.
  - **__init__.py**: Initializes the Flask app.
  - **routes.py**: Contains all the routes for different pages in the app.
  - **database.py**: Manages the connection to the SQLite database.
  - **static/**: Stores static assets like CSS.
  - **templates/**: HTML templates used to render the pages.
- **run.py**: The entry point to run the Flask server.
- **requirements.txt**: Lists all dependencies required for the project.
- **README.md**: Project overview and instructions (this file).

## Installation Instructions

### 1. Prerequisites
- **Python 3.6+**
- **pip** (Python package installer)

### 2. Clone the Repository
Clone the project to your local machine:
```bash
git clone https://github.com/arjunbojja1/expense-tracker.git
cd expense-tracker
```

### 3. Create a Virtual Environment
It is recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Dependencies
Install all required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Initialize the Database
Use the Python shell to create the SQLite database and the `transactions` table:
```bash
python
```
Then run the following code:
```python
import sqlite3
conn = sqlite3.connect('expense_tracker.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 type TEXT,
                 category TEXT,
                 amount REAL,
                 date TEXT,
                 description TEXT
             )''')
conn.commit()
conn.close()
exit()
```

### 6. Run the Application
To start the server, run the following command:
```bash
python run.py
```
Visit `http://127.0.0.1:5000/` in your web browser to access the application.

## Usage
- **Add Transaction**: Click on "Add Transaction" in the navigation bar, and fill in the details to add an income or expense.
- **View Transactions**: Click on "View Transactions" to see the complete history of transactions.

## Future Improvements
- **User Authentication**: Adding login functionality for multiple users.
- **Charts and Graphs**: Visual representation of income and expenses.
- **Budget Tracking**: Allow users to set monthly budgets and track spending.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions, feel free to reach out at [your-email@example.com].

