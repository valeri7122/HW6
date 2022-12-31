import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql= """
SELECT ROUND(AVG(estimate), 1) as avg_estimate
FROM estimates
"""


if __name__ == '__main__':
    print(execute_query(sql))
