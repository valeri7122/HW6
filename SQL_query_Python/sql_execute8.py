import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT teacher_name, ROUND(AVG(estimate), 1) as avg_estimate
FROM estimates
JOIN teachers as t ON teacher_id = t.id
JOIN subjects as sub ON subject_id = sub.id
GROUP BY teacher_name
"""


if __name__ == '__main__':
    print(execute_query(sql))
