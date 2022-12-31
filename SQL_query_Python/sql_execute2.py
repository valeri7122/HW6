import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(estimate), 1) as avg_estimate, subject, student_name
FROM estimates
JOIN students as s ON student_id = s.id
JOIN subjects as sub ON subject_id = sub.id  
GROUP BY subject, student_name
ORDER BY avg_estimate DESC, student_name
LIMIT 1
"""


if __name__ == '__main__':
    print(execute_query(sql))
