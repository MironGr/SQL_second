import sys
import sqlite3 as lite


def query_string_5():
    """
    5. Вывести покупателей (полное имя, номер телефона)
которые что-либо покупали, проживающих в одном городе,
если их кол-во в городе больше 1.
    :return:  data = cur.fetchall()
    """
    con = None
    data = {}

    query_string = '''
        SELECT c.FirstName, c.LastName, c.Phone, c.City, sum(i.Total)  
        FROM Customer AS c
        JOIN Invoice AS i ON c.CustomerId = i.CustomerId
        WHERE i.Total > 0 
        GROUP BY c.FirstName, c.LastName
        ORDER BY c.City
      '''

    try:
        con = lite.connect('vers_1.sqlite')
        cur = con.cursor()
        cur.execute(query_string)
        data = cur.fetchall()
        for line in data:
            print(line)
        return data
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if con:
            con.close()