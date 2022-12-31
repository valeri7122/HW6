import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT student_name, subject
FROM estimates
JOIN subjects as sub ON sub.id = subject_id
JOIN students as s ON s.id = student_id
WHERE student_name = 'Kelly Smith'
GROUP BY subject
"""


if __name__ == '__main__':
    print(execute_query(sql))
