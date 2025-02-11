import zipfile
import os

def package_changes(scripts, output_file):
    """
    Packages multiple SQL script files into a single ZIP archive.

    Parameters:
        scripts (list): A list of SQL script file paths to include in the ZIP.
        output_file (str): The path where the ZIP file will be created.
    """
    try:
        # Check if all script files exist before creating the ZIP
        missing_files = [script for script in scripts if not os.path.exists(script)]
        if missing_files:
            raise FileNotFoundError(f"❌ Missing files: {', '.join(missing_files)}")

        # Create the ZIP file
        with zipfile.ZipFile(output_file, 'w') as zf:
            for script in scripts:
                zf.write(script)
                print(f"✔ Added: {script}")

        print(f"🎉 Successfully packaged into {output_file}")

    except FileNotFoundError as e:
        print(f"🚨 Error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def main():
    """
    Defines SQL script paths and calls package_changes() to create the ZIP file.
    """
    script1 = 'schema_changes.sql'
    script2 = 'data_migration.sql'
    output_path = 'deployment_package.zip'
    
    scripts = [script1, script2]
    
    package_changes(scripts, output_path)

if __name__ == "__main__":
    main()