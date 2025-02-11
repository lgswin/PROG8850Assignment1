# . Describe the script’s functionality and how it handles the deployment process.

import zipfile
import pymysql
import os

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'rootpassword'  # 실제 비밀번호 입력
DB_NAME = 'assignment1'  # 실제 데이터베이스 이름 입력
PACKAGE_FILE = 'deployment_package.zip'  # 패키징된 ZIP 파일 경로

def deploy_database_changes():
    """
    Deploys database changes by extracting and executing SQL scripts from a ZIP package.
    """
    try:
        # Check if ZIP file exists
        if not os.path.exists(PACKAGE_FILE):
            raise FileNotFoundError(f"❌ Deployment package '{PACKAGE_FILE}' not found.")

        # Connect to MySQL database
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        print("✅ Connected to the database successfully.")

        # Open the ZIP file and process each SQL script
        with zipfile.ZipFile(PACKAGE_FILE, 'r') as zf:
            for script in zf.namelist():
                print(f"📂 Processing {script}...")
                with zf.open(script) as file:
                    sql_script = file.read().decode('utf-8')

                    # Split and execute SQL statements
                    statements = sql_script.split(';')
                    for statement in statements:
                        if statement.strip():  # Ignore empty statements
                            try:
                                cursor.execute(statement)
                                connection.commit()
                                print(f"✔ Executed: {statement[:50]}...")  # 첫 50자만 출력
                            except pymysql.MySQLError as e:
                                print(f"❌ Error executing: {statement[:50]}...\n{e}")

        print("🎉 Successfully deployed all SQL scripts!")

    except FileNotFoundError as e:
        print(f"🚨 Error: {e}")
    except pymysql.MySQLError as e:
        print(f"🚨 Database error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    finally:
        # Close database connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
        print("🔌 Database connection closed.")

if __name__ == "__main__":
    deploy_database_changes()