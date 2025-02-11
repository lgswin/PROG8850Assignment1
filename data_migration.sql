-- 1. Insert some example rows directly into 'employees_new'.
-- Manually inserting a few new records into 'employees_new'.
INSERT INTO employees_new (id, name, department, hire_date, email)
VALUES 
(101, 'Harpreet', 'HR', '2022-05-10', 'example1@example.com'),
(102, 'Davis', 'Engineering', '2021-07-22', 'example2@example.com'),
(103, 'Lisa', 'Finance', '2023-02-15', 'example3@example.com');

-- 2. Update existing records in 'employees_new' to correct or add email addresses.
-- Assuming you have an 'email_updates' table with new email addresses for some employees.
-- UPDATE employees_new en
-- JOIN email_updates eu ON en.id = eu.employee_id
-- SET en.email = eu.email;

-- 3. Add a new column to 'employees_new' table if needed.
-- Example: Adding a 'salary' column if it doesn't already exist.
ALTER TABLE employees_new ADD COLUMN salary DECIMAL(10, 2) NULL;

-- 4. Insert salary data for specific employees in 'employees_new'.
-- Example: Updating salary for recently added employees.
UPDATE employees_new
SET salary = CASE 
    WHEN id = 101 THEN 60000
    WHEN id = 102 THEN 75000
    WHEN id = 103 THEN 68000
    ELSE salary
END;

-- 6. Optionally, delete the archived employees from 'employees_new'.
-- Remove employees from the 'employees_new' table after archiving.
DELETE FROM employees_new
WHERE hire_date < '2020-01-01';

-- 7. Insert new departments into a 'departments' table.
-- Assuming a 'departments' table is being populated from a new system.
-- INSERT INTO departments (department_id, department_name)
-- VALUES
-- (1, 'Human Resources'),
-- (2, 'Engineering'),
-- (3, 'Finance');

-- 8. Add more operations for data transformations or clean-up as needed.
-- Example: Update some records to fix department names.
-- UPDATE employees_new
-- SET department = 'HR'
-- WHERE department = 'Human Resources';

-- 9. Commit the transaction if necessary (depending on your database environment).
-- COMMIT;
