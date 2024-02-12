SELECT g.grade
FROM Grades g
JOIN Students s ON g.student_id = s.id
JOIN Subjects sub ON g.subject_id = sub.id
JOIN Groups gr ON s.group_id = gr.id
WHERE gr.group_name = 'groupA' AND sub.subject_name = 'математика';

