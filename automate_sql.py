# Import the pymysql module
import pymysql  

# Database connection details
DB_HOST = 'localhost'  
DB_USER = 'root'  
DB_PASSWORD = 'rootpassword' 
DB_NAME = 'assignment1'  
SQL_SCRIPT_PATH = 'schema_changes.sql'  # sql script

try:
    # Create a connection to the MySQL database
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    print("Connected to the database successfully.")

    # Open the SQL script file
    with open(SQL_SCRIPT_PATH, 'r') as file:
        sql_script = file.read()

    # Create a cursor object
    cursor = connection.cursor()

    # Execute each SQL statement separately
    for statement in sql_script.split(';'):
        if statement.strip():  # Ignore empty statements
            try:
                cursor.execute(statement)
                print(f"Successfully executed: {statement[:50]}...")  # Print first 50 chars
            except pymysql.MySQLError as e:
                print(f"Error executing statement: {statement[:50]}... \n{e}")

    # Commit the changes
    connection.commit()
    print("🎉 All SQL statements executed successfully!")

except pymysql.MySQLError as e:
    print(f"Database connection error: {e}")

finally:
    # Ensure resources are released
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("🔌 Connection closed.")