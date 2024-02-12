SELECT DISTINCT sub.subject_name
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.id
JOIN Students s ON g.student_id = s.id
JOIN Teachers t ON sub.teacher_id = t.id
WHERE s.id = 1 AND t.id = 1;

