import sys
import sqlite3 as lite


def query_string_6():
    """
    6. Вывести топ 3 самых платежеспособных города за все время.
    :return:  data = cur.fetchall()
    """
    con = None
    data = {}

    query_string = '''
        SELECT i.BillingCity, sum(i.Total)  
        FROM Invoice AS i 
        GROUP BY i.BillingCity
        ORDER BY sum(i.Total) DESC
        LIMIT 3
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