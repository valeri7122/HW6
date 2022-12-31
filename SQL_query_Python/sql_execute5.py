import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT teacher_name, subject
FROM teachers as t
LEFT JOIN subjects as sub ON t.id = teacher_id
WHERE teacher_name = 'Jacob Becker'
"""


if __name__ == '__main__':
    print(execute_query(sql))
