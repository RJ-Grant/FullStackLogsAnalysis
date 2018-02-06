# Database code for the DB Forum, full solution!

import psycopg2
import bleach

DBNAME = "news"


def get_articles():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select a.title, count(*) as num
        from articles a,log b
        where b.path like '%' || a.slug || '%'
        and b.status = '200 OK'
        group by a.title, a.slug
        order by num desc limit 3;""")
    articles = c.fetchall()
    db.close()
    return articles


def get_authors():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select a.name, count(*) as num
        from authors a, articles b, log c
        where a.id = b.author and c.path like '%' || b.slug || '%'
        and c.status = '200 OK'
        group by a.name
        order by num desc limit 3;""")
    authors = c.fetchall()
    db.close()
    return authors


def get_errs():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select a.time,
        round(((b.num::numeric/a.total)*100),2) as percentage
        from requests a, ERR_status b
        where a.time = b.time and ((b.num::numeric/a.total)*100) > 1;""")
    errs = c.fetchall()
    db.close()
    return errs
