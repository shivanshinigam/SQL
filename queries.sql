
-- Q01: Question: Show all intern profiles 
SELECT * FROM internprofile;

-- Q02: Question: Show all internship postings
SELECT * FROM codecompanyinterns;

-- Q03: Question: Show all salary records 
SELECT * FROM internsalary;

-- Q04: Question: Show each intern's full name and email
SELECT first_name || ' ' || last_name AS name, email FROM internprofile;

-- Q05: Question: Which interns live in Pune?
SELECT * FROM internprofile WHERE city = 'Pune';

-- Q06: Question: Which interns have stipend more than 30000? 
SELECT p.first_name, p.last_name, s.stipend
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
WHERE s.stipend > 30000;

-- Q07: Question: How many interns does each company have? 
SELECT c.company_name, COUNT(s.intern_id) AS interns_count
FROM codecompanyinterns c
LEFT JOIN internsalary s ON c.internship_id = s.internship_id
GROUP BY c.company_name;

-- Q08: Question: What is the average stipend at each company? 
SELECT c.company_name, AVG(s.stipend) AS avg_stipend
FROM codecompanyinterns c
JOIN internsalary s ON c.internship_id = s.internship_id
GROUP BY c.company_name;

-- Q09: Question: Which companies currently have at least one intern? 
SELECT c.company_name, COUNT(s.intern_id) AS interns_count
FROM codecompanyinterns c
LEFT JOIN internsalary s ON c.internship_id = s.internship_id
GROUP BY c.company_name
HAVING COUNT(s.intern_id) > 0;

-- Q10: Question: What is the highest stipend any intern gets?
SELECT MAX(stipend) AS highest_stipend FROM internsalary;

-- Q11: Question: What is the lowest stipend recorded?
SELECT MIN(stipend) AS lowest_stipend FROM internsalary;

-- Q12: Question: What is the total of all stipends?
SELECT SUM(COALESCE(stipend,0)) AS total_stipend FROM internsalary;

-- Q13: Question: How many different universities do interns come from? 
SELECT COUNT(DISTINCT university) AS different_unis FROM internprofile;

-- Q14: Question: Show intern names and their company 
SELECT p.first_name, p.last_name, c.company_name
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
JOIN codecompanyinterns c ON s.internship_id = c.internship_id;

-- Q15: Question: Which internships have no interns assigned? 
SELECT c.company_name
FROM codecompanyinterns c
LEFT JOIN internsalary s ON c.internship_id = s.internship_id
WHERE s.salary_id IS NULL;

-- Q16: Question: Find pairs of interns from the same city 
SELECT a.intern_id AS id1, a.first_name || ' ' || a.last_name AS name1,
       b.intern_id AS id2, b.first_name || ' ' || b.last_name AS name2,
       a.city
FROM internprofile a
JOIN internprofile b ON a.city = b.city AND a.intern_id < b.intern_id;

-- Q17: Question: Show intern emails with a fallback when missing
SELECT first_name, last_name, COALESCE(email,'no-email@example.com') AS email_show
FROM internprofile;

-- Q18: Question: Find interns whose first name contains 'an' 
SELECT first_name, last_name FROM internprofile WHERE first_name LIKE '%an%';

-- Q19: Question: What are the top two stipends? 
SELECT stipend FROM internsalary ORDER BY stipend DESC LIMIT 2;

-- Q20: Question: Which interns earn more than the overall average stipend?
SELECT p.first_name, p.last_name, s.stipend
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
WHERE s.stipend > (SELECT AVG(stipend) FROM internsalary);

-- Q21: Question: Which companies have at least one intern?
SELECT company_name
FROM codecompanyinterns c
WHERE EXISTS (SELECT 1 FROM internsalary s WHERE s.internship_id = c.internship_id);

-- Q22: Question: List all places mentioned (cities and internship locations)
SELECT city AS place FROM internprofile
UNION ALL
SELECT location AS place FROM codecompanyinterns;

-- Q23: Question: Which universities have average stipend above 30000? 
SELECT p.university, AVG(s.stipend) AS avg_stip
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
GROUP BY p.university
HAVING AVG(s.stipend) > 30000;

-- Q24: Question: Show stipend ranking within each internship 
SELECT s.salary_id, s.internship_id, s.intern_id, s.stipend,
       RANK() OVER (PARTITION BY s.internship_id ORDER BY s.stipend DESC) AS rank_in_company
FROM internsalary s
ORDER BY s.internship_id, rank_in_company;

-- Q25: Question: Count interns per university and order by count 
SELECT university, COUNT(*) AS interns_count
FROM internprofile
GROUP BY university
ORDER BY interns_count DESC;

-- Q26: Question: For each city show average and max stipend
SELECT p.city, AVG(s.stipend) AS avg_stip, MAX(s.stipend) AS max_stip
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
GROUP BY p.city
ORDER BY avg_stip DESC;

-- Q27: Question: For each company show number of interns and average work hours 
SELECT c.company_name, COUNT(s.intern_id) AS interns_count, AVG(s.work_hours) AS avg_hours
FROM codecompanyinterns c
LEFT JOIN internsalary s ON c.internship_id = s.internship_id
GROUP BY c.company_name;

-- Q28: Question: Which companies have average stipend above the overall average?
SELECT c.company_name, AVG(s.stipend) AS avg_stip
FROM codecompanyinterns c
JOIN internsalary s ON c.internship_id = s.internship_id
GROUP BY c.company_name
HAVING AVG(s.stipend) > (SELECT AVG(stipend) FROM internsalary);

-- Q29: Question: Show interns working more than 35 hours with their company
SELECT p.first_name || ' ' || p.last_name AS name, c.company_name, s.work_hours
FROM internprofile p
JOIN internsalary s ON p.intern_id = s.intern_id
JOIN codecompanyinterns c ON s.internship_id = c.internship_id
WHERE s.work_hours > 35;

-- Q30: count internships per intern
SELECT p.intern_id, p.first_name || ' ' || p.last_name AS name, COUNT(s.internship_id) AS internships_count
FROM internprofile p
LEFT JOIN internsalary s ON p.intern_id = s.intern_id
GROUP BY p.intern_id
ORDER BY internships_count DESC;
