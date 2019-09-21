#!/usr/bin/python

import psycopg2
from datetime import datetime


def get_most_popular_3views_article():
    try:
        db = psycopg2.connect(database='news')
        c = db.cursor()
        sql_query = """select '"'||B.title||'" -- '|| A.view_count||' views'
                              as result
                       from (select replace(path,'/article/','') as slug,
                             count(id) as view_count
                            from log
                            where path != '/' and status = '200 OK'
                            group by replace(path,'/article/','') ) A
                        join articles           B on A.slug = B.slug
                        order by A.view_count desc
                        limit 3"""

        c.execute(sql_query)
        res = c.fetchall()
        db.close()
        # print(res)
        for e in res:
            print(e[0])
    except Exception as e:
        print(e)


def get_most_popular_authors_article():
    try:

        db = psycopg2.connect(database='news')
        c = db.cursor()
        sql_query = """select  C.name, count(A.id) as view_count
                        from (select replace(path,'/article/','') as slug,id
                            from log
                            where path != '/' and status = '200 OK'  ) A
                        join articles                      B on A.slug = B.slug
                        join authors                       C on B.author = C.id
                        group by C.name
                        order by view_count desc
                        """

        c.execute(sql_query)
        res = c.fetchall()
        db.close()
        # print(res)
        for e in res:
            output = e[0] + ' -- ' + str(e[1]) + ' views'
            print(output)
    except Exception as e:
        print(e)


def get_error_date():
    try:
        db = psycopg2.connect(database='news')
        c = db.cursor()
        sql_query = """
        select A.date,
        100*cast(error_count as decimal)/cast(ttl_count as decimal)
        from
        (select  date(time) as date, count(status) AS ttl_count,
        count(case when status != '200 OK' then 1 else null end) as error_count
        from log
        group by date) A
        where ttl_count * 0.01 - error_count < 0
                    """
        c.execute(sql_query)
        res = c.fetchall()
        db.close()
        # print(res)
        for e in res:
            d = datetime.strftime(e[0], '%b %d, %Y')
            output = d + ' -- ' + '{:.1f}%'.format(e[1]) + ' errors'
            print(output)
    except Exception as e:
        print(e)


print('Printing the most popular three articles of all time')
get_most_popular_3views_article()
print('\n')

print('Printing the most popular article authors of all time')
get_most_popular_authors_article()
print('\n')

print('Printing the days did more than 1% of requests lead to errors')
get_error_date()
print('\n')
