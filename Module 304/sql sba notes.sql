#8
SELECT s.firstname as "First Name",
s.lastname as "Last Name",
COUNT(sc.courseId) as "Number of Courses"
FROM student s
LEFT JOIN studentCourse sc ON s.id = sc.studentId
LEFT JOIN course c ON sc.courseId = c.id
LEFT JOIN department d ON c.deptId = d.id
GROUP BY c.deptId, s.majorId, s.firstname, s.lastname
HAVING c.deptId = s.majorId
ORDER BY COUNT(sc.courseId) DESC, s.firstname, s.lastname;

#9
SELECT s.firstname as "First Name",
s.lastname as "Last Name",
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM student s
LEFT JOIN studentCourse sc ON s.id = sc.studentId
LEFT JOIN course 
GROUP BY sc.progress, s.firstname, s.lastname
HAVING AVG(sc.progress) < 50
ORDER BY AVG(sc.progress) DESC, s.firstname, T1.lastname;

select distinct(c.name) as "Course Name", 
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM studentCourse sc
INNER JOIN course c ON sc.courseId = c.id
GROUP BY sc.studentId
HAVING AVG(sc.progress) < 50
ORDER BY AVG(sc.progress) DESC, c.name;
-- this works here but not in hackerrank WHY


select distinct(c.name) as "Course Name", 
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM studentCourse sc
INNER JOIN course c ON sc.courseId = c.id
INNER JOIN 
GROUP BY sc.studentId
HAVING AVG(sc.progress) < 50
ORDER BY AVG(sc.progress) DESC, c.name;

SELECT * FROM studentcourse sc
JOIN course c on sc.courseId = c.id
GROUP BY sc.studentId;


SELECT c.id,
       s.id,
       AVG(t.average_test_score) AS average_student_score
FROM course c
JOIN studentCourse sc ON c.id = t.courseId
JOIN (
    SELECT studentId, courseId, AVG(progress) AS average_test_score
    FROM studentCourse
    GROUP BY studentId, courseId
) AS t ON t.studentId = t.studentId AND t.courseId = c.id
JOIN student s ON s.id = t.studentId
GROUP BY c.id, s.id;

#10
SELECT T1.name as "Course Name",
ROUND(AVG(T2.progress), 1) as "Average Progress"
FROM course T1
LEFT JOIN studentCourse T2 ON T1.id = T2.courseId
GROUP BY T1.name
ORDER BY AVG(T2.progress) DESC, T1.name;

SELECT T1.name as "Course Name",
ROUND(AVG(T2.progress), 1) as "Average Progress"
FROM course T1
LEFT JOIN studentCourse T2 ON T1.id = T2.courseId
LEFT JOIN student T3 ON T2.studentId = T3.id
GROUP BY T3.id, T1.name
ORDER BY AVG(T2.progress) DESC, T1.name;


SELECT T1.name as "Course Name",
ROUND(AVG(T2.progress), 1) as "Average Progress"
FROM course T1
LEFT JOIN studentCourse T2 ON T1.id = T2.courseId
INNER JOIN (SELECT distinct(id) from student T3) AS Z ON T2.studentId = Z.id
GROUP BY Z.id, T1.name
ORDER BY AVG(T2.progress) DESC, T1.name;

-- Calculate the average test grade for each student
SELECT s.id,
		AVG(sc.progress) AS average_test_grade
FROM student s
JOIN studentCourse sc ON s.id = sc.studentId
GROUP BY s.id;

-- Calculate the overall average grade
SELECT AVG(average_test_grade) AS overall_average_grade
FROM (
    SELECT AVG(progress) AS average_test_grade
    FROM studentCourse
    GROUP BY studentId
) AS avg_grades;

-- do for all courses


SELECT T1.name as "Course Name",
ROUND(AVG(T2.progress)), 1) as "Average Progress"
FROM course T1
LEFT JOIN studentCourse T2 ON T1.id = T2.courseId
--LEFT JOIN student T3 ON T2.studentId = T3.id
INNER JOIN (SELECT distinct(id) from student T3) AS Z ON T2.studentId = Z.id
GROUP BY Z.id, T1.name
ORDER BY AVG(T2.progress) DESC, T1.name;

SELECT studentId, progress from studentcourse;



SELECT f.firstname as "First Name",
f.lastname as "Last Name",
ROUND(avg(sc.progress), 1) as "Average Progress"
FROM faculty f
INNER JOIN facultyCourse fc ON f.id = fc.facultyId
INNER JOIN studentCourse sc ON fc.courseId = sc.courseId
group by sc.courseId, f.firstname, f.lastname
order by avg(sc.progress) DESC, f.firstname, f.lastname;

SELECT distinct(fc.facultyId), 
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM facultycourse fc
INNER JOIN studentcourse sc ON fc.courseId = sc.courseId
GROUP BY fc.courseId
ORDER BY AVG(sc.progress) DESC;

SELECT distinct(f.firstname),
f.lastname, 
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM facultycourse fc
INNER JOIN studentcourse sc ON fc.courseId = sc.courseId
INNER JOIN faculty f ON fc.facultyId = f.id
GROUP BY fc.courseId
ORDER BY AVG(sc.progress) DESC, f.firstname, f.lastname;



#12
SELECT f.firstname as "First Name",
f.lastname as "Last Name",
ROUND(AVG(sc.progress), 1) as "Average Progress"
FROM faculty f
INNER JOIN 


