import sqlite3

class ExpenseDatabase:
    def __init__(self, db_name="expenses.db"):
    
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
       
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT DEFAULT CURRENT_DATE
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, description, amount):
        
        query = "INSERT INTO expenses (description, amount) VALUES (?, ?)"
        self.conn.execute(query, (description, amount))
        self.conn.commit()

    def get_all_expenses(self):
       
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, description, amount, date FROM expenses ORDER BY date DESC")
        return cursor.fetchall()

    def get_total_expenses(self):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM expenses")
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0.0

    def close(self):
        
        self.conn.close()
