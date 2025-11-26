CREATE TABLE codecompanyinterns (
  internship_id INTEGER PRIMARY KEY,
  company_name TEXT,
  position TEXT,
  location TEXT,
  start_date TEXT
);

CREATE TABLE internprofile (
  intern_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  university TEXT,
  graduation_year INTEGER,
  city TEXT
);

CREATE TABLE internsalary (
  salary_id INTEGER PRIMARY KEY,
  internship_id INTEGER,
  intern_id INTEGER,
  stipend INTEGER,
  work_hours INTEGER
);

INSERT INTO codecompanyinterns VALUES
(1, 'Code', 'Backend Intern', 'Bengaluru', '2025-12-01'),
(2, 'Data', 'Data Science Intern', 'Pune', '2025-11-10'),
(3, 'Gamers', 'Frontend Intern', 'Remote', '2025-10-01');

INSERT INTO internprofile VALUES
(101, 'Asha', 'Patel', 'asha@example.com', 'IIT Bombay', 2026, 'Mumbai'),
(102, 'Rohan', 'Verma', 'rohan@example.com', 'BITS Pilani', 2025, 'Pune'),
(103, 'Simran', 'Kaur', 'simran@example.com', 'IIIT Hyderabad', 2026, 'Hyderabad');

INSERT INTO internsalary VALUES
(1001, 1, 101, 30000, 40),
(1002, 2, 102, 35000, 38),
(1003, 3, 103, 28000, 30);
