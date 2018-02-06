#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from catalogdb import get_articles, get_authors, get_errs

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Your Catalog Report!</title>
    <style>
      h2, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <!-- top three articles -->
    <h2>Top Three Articles: </h2>
    <ol>
        %s
    </ol>
    <hr>
    <!-- top three authors -->
    <h2>Most Popular Authors</h2>
    <ol>
        %s
    </ol>
    <hr>
    <!-- top three authors -->
    <h2>Days with more than 1%% request errors</h2>
    <ul>
        %s
    </ul>
  </body>
</html>
'''

# HTML template for an individual comment
ARTICLES = '''\
    <li>%s - %s views</li>
'''
AUTHORS = '''\
    <li>%s - %s views</li>
'''
ERRORS = '''\
    <li>%s - %s %% errors</li>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    articles = "".join(ARTICLES % (title, num)
                       for title, num in get_articles())
    authors = "".join(AUTHORS % (name, num) for name, num in get_authors())
    errors = "".join(ERRORS % (time, percentage)
                     for time, percentage in get_errs())
    html = HTML_WRAP % (articles, authors, errors)
    return html


@app.route('/', methods=['POST'])
def post():
    '''New post submission.'''
    message = request.form['content']
    add_post(message)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
