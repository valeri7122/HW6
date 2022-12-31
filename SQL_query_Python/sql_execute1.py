import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(estimate), 1) as avg_estimate, student_name
FROM estimates
JOIN students as s ON student_id = s.id
GROUP BY student_name
ORDER BY avg_estimate DESC
LIMIT 5
"""


if __name__ == '__main__':
    print(execute_query(sql))
