import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT student_name, teacher_name, subject
FROM estimates
JOIN students as s ON student_id = s.id
JOIN subjects as sub ON subject_id = sub.id
JOIN teachers as t ON teacher_id = t.id
WHERE student_name = "Robin Koch" AND teacher_name = 'Robert Cameron'
GROUP BY subject 
"""


if __name__ == '__main__':
    print(execute_query(sql))
