import psycopg2
import bleach

DBNAME = "news"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print("1. What are the most popular three articles of all time?\n")
    c.execute("select articles.title, n2.count from articles, (select path, \
    count(path) from log where STATUS='200 OK' and method='GET' \
    and path != '/' group by path order by count(path) desc limit 3) \
    as n2 where concat ('/article/', articles.slug) = n2.path \
    order by n2.count desc")
    result = c.fetchall()
    for item in result:
        print(str(item[0]) + " - "  + str(item[1]) + " views")
    print ("\n")
    c.execute("select authors.name as author, n3.count from authors, \
    (select articles.author, sum(n2.count) as count from articles, \
    (select path, count(path) from log where status = '200 OK' \
    and method = 'GET' and path !='/' group by path order by \
    count(path) desc) as n2 where n2.path = concat ('/article/', slug) \
    group by articles.author order by sum(n2.count) desc) as n3 \
    where authors.id = n3.author")
    result = c.fetchall()
    print("2.Who are the most popular article authors of all time?\n")
    for item in result:
        print(str(item[0]) + " - "  + str(item[1]))
    print("\n")
    print("3.On which days did more than 1% of requests lead to errors?\n")
    c.execute("select round(numer.error*100.0/denom.total, 2) as percentage,\
    denom.date from (select count(*) AS total , to_char(time, 'DD Mon YYYY') \
    as date from log group by 2) as denom,  (select count(status) as error , \
    to_char(time, 'DD Mon YYYY') as date from log where \
    status != '200 OK' group by 2) as numer where \
    numer.date = denom.date and numer.error*100.0/denom.total > 1")
    result = c.fetchall()
    for item in result:
        print (str(item[1]) + " - " + str(item[0]) + " % errors")
    db.close()


if __name__ == '__main__':
    get_posts()
