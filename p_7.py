import sys
import sqlite3 as lite


def query_string_7():
    """
    7. Вывести самый популярный, на основании кол-ва продаж,
    жанр (название) и все треки в нем (название, альбом, исполнитель)
    :return:  data = cur.fetchall()
    """
    con = None
    data = {}

    query_string = '''
        SELECT g.Name, t.Name, al.Title, ar.Name, sum(il.Quantity)  
        FROM Genre AS g
        JOIN Track AS t ON g.GenreId = t.GenreId
        JOIN InvoiceLine AS il ON t.TrackId = il.TrackId
        JOIN Album AS al ON t.AlbumId = al.AlbumId
        JOIN Artist AS ar ON al.ArtistId = ar.ArtistId
        GROUP BY g.Name
        ORDER BY sum(il.Quantity) DESC
        LIMIT 1
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