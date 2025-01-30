import subprocess

# MySQL container information
container_name = "mysql_container"
sql_files = ["create.sql", "books.sql"]  # SQL files to run
container_sql_path = "/tmp"  # the path inside the container

try:
    # copy sql files into the container
    for sql_file in sql_files:
        print(f"📂 Copying {sql_file} to Docker container...")
        subprocess.run(f"docker cp {sql_file} {container_name}:{container_sql_path}/{sql_file}", shell=True, check=True)

    # run mysql and sql files
    for sql_file in sql_files:
        print(f"🚀 Executing {sql_file} inside Docker container...")
        mysql_command = f"docker exec {container_name} sh -c 'mysql -u root -p\"rootpassword\" < {container_sql_path}/{sql_file}'"
        subprocess.run(mysql_command, shell=True, check=True)

    print("All SQL scripts executed successfully!")

except subprocess.CalledProcessError as e:
    print(f"Error executing SQL scripts: {e}")