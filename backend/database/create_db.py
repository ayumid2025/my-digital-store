import sqlite3

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('database/store.db')
cursor = conn.cursor()

# Create a table called 'users' with columns: id, username, password
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()

print("Database and users table created successfully!")
