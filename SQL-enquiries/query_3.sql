SELECT AVG(grade) AS avg_rate
FROM Grades g2
JOIN Students AS s ON g2.student_id = s.id
JOIN Groups AS grp ON s.group_id = grp.id
JOIN Subjects AS sub ON g2.subject_id = sub.id
WHERE sub.id = 2

