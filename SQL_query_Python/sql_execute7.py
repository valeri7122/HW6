import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT date_of, student_name, group_number, subject, estimate
FROM estimates
JOIN students as s ON student_id = s.id
JOIN groups as g ON group_id = g.id
JOIN subjects as sub ON subject_id = sub.id
WHERE subject = "History" AND group_number = 3
ORDER BY student_name
"""


if __name__ == '__main__':
    print(execute_query(sql))
