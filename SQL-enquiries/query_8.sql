SELECT t.name AS teacher_name, AVG(g.grade) AS avg_grade
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.id
JOIN Teachers t ON sub.teacher_id = t.id
GROUP BY t.name;
