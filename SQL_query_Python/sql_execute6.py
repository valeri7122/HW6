import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT student_name, group_number
FROM students
JOIN groups ON groups.id = group_id
WHERE group_number = 2
ORDER BY student_name
"""


if __name__ == '__main__':
    print(execute_query(sql))
