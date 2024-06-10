1.  --create new db, companydb--
CREATE DATABASE companydb;

2.  --switch to the new db--
USE companydb;

3.  --create table--
CREATE TABLE projects(
    id AUTO-INCREMENT PRIMARY KEY,
    project_name VARCHAR(50),
    start_date DATE,
    end_date DATE,
    budget FLOAT
    );
    
4.  --insert sample data--
INSERT INTO projects(project_name, start_date, end_date, budget) VALUES('Construction', '2023-05-11', '2024-07-22', 70000000);

INSERT INTO projects(project_name, start_date, end_date, budget) VALUES('Digging', '2023-08-19', '2024-09-28', 800000);

INSERT INTO projects(project_name, start_date, end_date, budget) VALUES('Project Alpha', '2023-08-19', '2024-19-08', 100000);

5. /*Write select queries for the following*/
--retrieve all projects--
SELECT * FROM projects;

--retrieve only 'project_name and 'budget' for all projects--
SELECT project_name, budget FROM projects;

--retrieve projects with a budget greater than 60000--
SELECT * FROM projects WHERE budget>60000;

--sort projects by 'start_date' in ascending order--
SELECT * FROM projects ORDER BY start_date ASC;

6. update budget for 'Project Alpha' to 120000--
UPDATE projects SET budget=120000 WHERE project_name='Project Alpha';

7. --delete 'Project Gamma--
DELETE FROM projects WHERE project_name='Digging';

