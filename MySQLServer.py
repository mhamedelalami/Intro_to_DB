import mysql.connector
import mysql.connector

try:
    # Connect to MySQL server (without selecting a specific database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sql2143!.'  # Replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Properly close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
